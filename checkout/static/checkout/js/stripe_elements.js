/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment

    CSS from here: 
    https://stripe.com/docs/stripe-js
*/

// Load Stripe public key and client secret from hidden elements in the template
const stripePublicKey = $('#id_stripe_public_key').text().trim();
const clientSecret = $('#id_client_secret').text().trim();

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