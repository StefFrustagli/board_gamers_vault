/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment

    CSS from here: 
    https://stripe.com/docs/stripe-js
*/

// Load Stripe public key and client secret from hidden elements in the template
const stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
const clientSecret = $('#id_client_secret').text().slice(1, -1);

// Initialize Stripe with the public key
const stripe = Stripe(stripePublicKey);

// Create a new instance of Elements
const elements = stripe.elements();

// Define custom styling for the card element
const style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};

// Create a Card Element with custom styling
const card = elements.create('card', { style });

// Mount the Card Element to the card-element container in the template
card.mount('#card-element');

// Handle realitine validation errors on the card element
card.addEventListener("change", function (event) {
  const errorDiv = document.getElementById("card-errors");
  if (event.error) {
    const html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
    $(errorDiv).html(html);
  } else {
    errorDiv.textContent = "";
  }
});

// Handle form submit
const form = document.getElementById('payment-form');

form.addEventListener("submit", async function (ev) {
  ev.preventDefault();
  card.update({ disabled: true });
  $("#submit-button").attr("disabled", true);
  // Toggles the visibility of the payment form with fade effect 
  $("#payment-form").fadeToggle(100);
  // Toggles the visibility of the loading overlay with fade effect 
  $("#loading-overlay").fadeToggle(100);

  // const saveInfo = Boolean($("#id-save-info").attr("checked"));
  const saveInfo = $("#id-save-info").is(":checked"); 
  // From using {% csrf_token %} in the form
  const csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
  const postData = {
    csrfmiddlewaretoken: csrfToken,
    client_secret: clientSecret,
    save_info: saveInfo,
  };
  const url = "/checkout/cache_checkout_data/";

  try {
    $.post(url, postData)
      .done(async function () {
        const result = await stripe.confirmCardPayment(clientSecret, {
          payment_method: {
            card: card,
            billing_details: {
              name: $.trim(form.full_name.value),
              phone: $.trim(form.phone_number.value),
              email: $.trim(form.email.value),
              address: {
                line1: $.trim(form.street_address1.value),
                line2: $.trim(form.street_address2.value),
                city: $.trim(form.town_or_city.value),
                country: $.trim(form.country.value),
                state: $.trim(form.county.value),
              },
            },
          },
          shipping: {
            name: $.trim(form.full_name.value),
            phone: $.trim(form.phone_number.value),
            address: {
              line1: $.trim(form.street_address1.value),
              line2: $.trim(form.street_address2.value),
              city: $.trim(form.town_or_city.value),
              country: $.trim(form.country.value),
              postal_code: $.trim(form.postcode.value),
              state: $.trim(form.county.value),
            },
          },
        });

        if (result.error) {
          const errorDiv = document.getElementById("card-errors");
          errorDiv.textContent = result.error.message;
          card.update({ disabled: false });
          $("#submit-button").attr("disabled", false);
          $("#payment-form").fadeToggle(100); // ENSURING SPINNER STOPS
          $("#loading-overlay").fadeToggle(100); // ENSURING SPINNER STOPS
        } else {
          if (result.paymentIntent.status === "succeeded") {
            form.submit();
          }
        }
      })
      .fail(function () {
        // Handle failure in caching checkout data
        location.reload();
      });
  } catch (error) {
    console.error("Error:", error);
    // Handle error gracefully, show a message to the user or log it
    const errorDiv = document.getElementById("card-errors");
    errorDiv.textContent = "An error occurred. Please try again later.";
    // Toggles the visibility of the payment form with a fade effect over 100 milliseconds
    $("#payment-form").fadeToggle(100);
    // Toggles the visibility of the loading overlay with a fade effect over 100 milliseconds
    $("#loading-overlay").fadeToggle(100);
    card.update({ disabled: false });
    $("#submit-button").attr("disabled", false);
  }
});