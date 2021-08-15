from django.test import TestCase



class TolokaAccountKeysTestCase(TestCase):
    form_url: str = '/get_form'



    def test_bad_result_sravnenie_form_s_validaciey_dannyh(self):
        response = self.client.post(self.form_url, data={
            "field_name_1": 'infodo@edu.mos.ru',


        })

        self.assertEqual(response.status_code, 400)



    def test_ok_result_sravnenie_form_s_validaciey_dannyh(self):
        response = self.client.post(self.form_url, data={
            "field_name_1": 'abc@mail.ru',
            "field_name_2": '+7 926 520 97 64'

        })

        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertEqual(response_data["name_form_template"], "Form template name 5")

    def test_ok_result_vyvod_informacii_o_dannyh_ne_proshedshih_validaciu_1(self):
        response = self.client.post(self.form_url, data={        # аналог того что мы делаем в браузере
            "field_name_1": 'abcmail.ru',
            "field_name_2": '+ 926 520 97 64'
        })

        self.assertEqual(response.status_code, 400)
#        response_data = response.json()
#        self.assertEqual(response_data, 'Form template name 5')

    def test_ok_result_vyvod_informacii_o_dannyh_ne_proshedshih_validaciu_2 (self):
        response = self.client.post(self.form_url, data={        # аналог того что мы делаем в браузере
            "field_name_1": 'abc@mail.ru',
            "field_name_2": '+ 926 520 97 64'
        })

        self.assertEqual(response.status_code, 400)