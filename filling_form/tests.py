from django.test import TestCase


"""
в тестах происходит обращение к урлам, эндпоинтам 
это не правило а сложиваяся практика
поэтому все урлы выносятися в атрибуты класса
какие - либо константные данные лучше выноситьь в атрибуты класса 
"""
class TolokaAccountKeysTestCase(TestCase):
    form_url: str = '/get_form'                       # создаем константу к которой будем обращаться



    def test_bad_result_sravnenie_form_s_validaciey_dannyh(self):
        response = self.client.post(self.form_url, data={        # аналог того что мы делаем в браузере
            "field_name_1": 'infodo@edu.mos.ru',


        })

        self.assertEqual(response.status_code, 400)



    def test_ok_result_sravnenie_form_s_validaciey_dannyh(self):
        response = self.client.post(self.form_url, data={        # аналог того что мы делаем в браузере
            "field_name_1": 'abc@mail.ru',
            "field_name_2": '+7 926 520 97 64'

        })

        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertEqual(response_data["name"], "Form template name 5")

    def test_ok_result_poluchenie_spiska_kluchey(self):
        response = self.client.post(self.form_url, data={        # аналог того что мы делаем в браузере
            "field_name_1": 'abc@mail.ru',
            "field_name_2": '+7 926 520 97 64'
        })


        keys_query_test = response.data.keys()
        self.assertEqual(keys_query_test["field_name_1"], 'abc@mail.ru')




# def setUp(self):                                       # сделай какие-то действия перед каждым тестом
    #     self.first_user = UserFactory()
    #     self.second_user = UserFactory()
    #     self.patcher = patch(
    #         'tolokamanager.api_service.service.TolokaService.get_toloka_data',
    #         Mock(return_value=self.regular_toloka_responce)
    #     )
    #     self.mock_foo = self.patcher.start()
    #     self.client.force_login(self.first_user)
    #
     # def tearDown(self) -> None:                                #  метод обратный set up   выполнить дейсствия заверщающие
     #    self.client.logout()
     #    self.patcher.stop()

    # @staticmethod                                                    # это динамические урлы
    # def _get_token_url(token_account_id) -> str:
    #     return reverse(
    #         'toloka_manager_api:tolokaaccount-detail', kwargs={'pk': token_account_id}
    #     )
    #
    # @staticmethod
    # def _get_token_share_url(token_account_id) -> str:
    #     return reverse(
    #         'toloka_manager_api:tolokaaccount-share', kwargs={'pk': token_account_id}
    #     )
    #
    # @staticmethod
    # def _get_token_set_current_url(token_account_id) -> str:
    #     return reverse(
    #         'toloka_manager_api:tolokaaccount-set-current', kwargs={'pk': token_account_id}
    #     )







