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

form.addEventListener('submit', async function(ev) {
    ev.preventDefault();
    card.update({ 'disabled': true });
    $('#submit-button').attr('disabled', true);

    try {
        const result = await stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
            }
        });

        if (result.error) {
            const errorDiv = document.getElementById('card-errors');
            errorDiv.textContent = result.error.message;
            card.update({ 'disabled': false });
            $('#submit-button').attr('disabled', false);
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    } catch (error) {
        console.error('Error:', error);
        // Handle error gracefully, show a message to the user or log it
        const errorDiv = document.getElementById('card-errors');
        errorDiv.textContent = 'An error occurred. Please try again later.';
        card.update({ 'disabled': false });
        $('#submit-button').attr('disabled', false);
    }
});