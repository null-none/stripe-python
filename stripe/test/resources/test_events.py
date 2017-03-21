import stripe
from stripe.test.helper import (
    StripeResourceTest,
    SAMPLE_EVENT_PAYLOAD,
    SAMPLE_EVENT_SIGNATURE_SECRET,
    SAMPLE_EVENT_SIGNATURE,
)


class EventTest(StripeResourceTest):

    def test_verify_valid_signature(self):
        event = stripe.Event.verify_signature(SAMPLE_EVENT_PAYLOAD,
                                              SAMPLE_EVENT_SIGNATURE_SECRET,
                                              SAMPLE_EVENT_SIGNATURE)
        self.assertTrue(isinstance(event, stripe.Event))
        self.assertEqual('evt_test', event.id)

    def test_verify_invalid_signature(self):
        with self.assertRaises(Exception):
            stripe.Event.verify_signature(SAMPLE_EVENT_PAYLOAD,
                                          SAMPLE_EVENT_SIGNATURE_SECRET,
                                          'definitelynottherealsignature')
