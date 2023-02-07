from django.test import TestCase
import django.core.mail as mail
from eventex.subscriptions.forms import SubscriptionForm

# Create your tests here.

class SubscribeTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/inscricao/')

    def test_get(self):
        """Get /inscricao/ must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must use subscriptions/templates/subscriptions_form.html"""
        self.assertTemplateUsed(self.response, 'subscription_form.html')

    def test_html(self):
        """Html must contain input tags"""
        self.assertContains(self.response, '<form')
        self.assertContains(self.response, '<input', 6)
        self.assertContains(self.response, 'type="text"', 3)
        self.assertContains(self.response, 'type="email"')
        self.assertContains(self.response, 'type="submit"')

    def test_csrf(self):
        """Html mist contain crsf"""
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """Context must have subscription form"""
        form = self.response.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_form_has_field(self):
        """Form must have 4 fields"""
        form = self.response.context['form']
        self.assertSequenceEqual(['name', 'cpf', 'email', 'phone'], list(form.fields))

class SubscribePostTest(TestCase):
    def setUp(self):
        data = dict(name='Henrique Bastos', cpf='12345678901',
        email='henrique@bastos.net', phone='21-99618-6180')
        self.response = self.client.post('/inscricao/', data)

        self.email = mail.outbox[0]

    def test_post(self):
        """Valid POST should redirect to /incricao/"""
        self.assertEqual(302, self.response.status_code)

    def test_send_subscribe_email(self):
        """Send mail"""
        self.assertEqual(1, len(mail.outbox))

    def test_subscription_email_subject(self):
        """Mail subject"""
        expect = 'Confirmação de inscrição'
        
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        """Email from"""
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)
    
    def test_subscription_email_to(self):
        """Email to"""

        expect = ['contato@eventex.com.br', 'henrique@bastos.net']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        """Email body"""

        self.assertIn('Henrique Bastos', self.email.body)
        self.assertIn('12345678901', self.email.body)
        self.assertIn('henrique@bastos.net', self.email.body)
        self.assertIn('21-99618-6180', self.email.body)
        
class SubscribeInvalidPost(TestCase):
    def setUp(self):
        self.response = self.client.post('/inscricao/', {})

    def test_post(self):
        """Invalid POST should not redirect"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'subscription_form.html')

    def test_has_form(self):
        form = self.response.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_form_has_erros(self):
        form = self.response.context['form']
        self.assertTrue(form.errors)

class SubscribeSucessMessage(TestCase):
    def test_message(self):
        data = dict(name='Henrique Bastos', cpf='12345678901',
        email='henrique@bastos.net', phone='21-99618-6180')

        response = self.client.post('/inscricao/', data, follow=True)
        self.assertContains(response, 'Inscrição realizada com sucesso!')