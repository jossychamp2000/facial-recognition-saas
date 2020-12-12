let DEBUG = false;
let host = "http://127.0.0.1:8000";
let stripePublishKey = "pk_test_51GvuhsG2pgXqIT36lRYvFTt6qFMoO6pnEoAZSTBm00EQ7HDEx1FbIEPf0pqF6bAULYWdJupKNZt8yIvuVpn5Odhw00x8jbEPmC";
if (DEBUG === false) {
  host = "http://138.197.134.237";
  stripePublishKey = "pk_test_51GvuhsG2pgXqIT36lRYvFTt6qFMoO6pnEoAZSTBm00EQ7HDEx1FbIEPf0pqF6bAULYWdJupKNZt8yIvuVpn5Odhw00x8jbEPmC";
}

export { stripePublishKey };

export const APIEndpoint = `${host}/api`;

export const fileUploadURL = `${APIEndpoint}/demo/`;
export const facialRecognitionURL = `${APIEndpoint}/upload/`;
export const emailURL = `${APIEndpoint}/email/`;
export const changeEmailURL = `${APIEndpoint}/change-email/`;
export const changePasswordURL = `${APIEndpoint}/change-password/`;
export const billingURL = `${APIEndpoint}/billing/`;
export const subscribeURL = `${APIEndpoint}/subscribe/`;
export const APIkeyURL = `${APIEndpoint}/api-key/`;
export const cancelSubscriptionURL = `${APIEndpoint}/cancel-subscription/`;

export const loginURL = `${host}/rest-auth/login/`;
export const signupURL = `${host}/rest-auth/registration/`;
