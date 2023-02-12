from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm

class SubscriptionFormTest(TestCase):

    def test_has_field(self):
        """Form must have 4 fields"""
        form = SubscriptionForm()
        expected = ['name', 'cpf', 'email', 'phone']
        self.assertSequenceEqual(expected, list(form.fields))

    def test_cpf_is_digit(self):
        """CPF must only accpet digits."""
        form = self.make_validated_form('ABCD5678901')
        self.assertFormErrorCode(form, 'cpf', 'digits')

    def test_cpf_has_11_digits(self):
        """CPF must have 11 digits."""
        form = self.make_validated_form('1234')
        self.assertFormErrorCode(form, 'cpf', 'length')

    def assertFormErrorCode(self, form, field, code):
        errors = form.errors.as_data()
        errors_list = errors[field]
        exception = errors_list[0]
        self.assertEqual(code, exception.code)

    def make_validated_form(self, cpf):
        data = dict(
            name = 'Henrique Bastos',
            cpf = cpf,
            email = 'henrique@bastos.net',
            phone = '21-996186180'
        )

        form = SubscriptionForm(data)
        form.is_valid()

        return form