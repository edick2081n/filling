from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseBadRequest, JsonResponse
from django.urls import reverse
import json
import re


def form_list(request):
    return render(request, "filling_form/form_list.html")


def zapros(request):
    if request.method == 'POST':
        query_post = request.POST
        keys_query = list(query_post.keys())
        values_query = list(query_post.values())
        del keys_query[0]

        file_json = open("db.json", encoding="utf8")
        list_json = json.load(file_json)

        current_template = None
        keys_count = 0
        for form_template in list_json:
            current_template_field_set = set(form_template.keys())
            current_template_field_set.remove('name')
            if current_template_field_set <= set(keys_query):
                current_form_keys_count = len(current_template_field_set)
                if current_form_keys_count > keys_count:
                    current_template = form_template

        if current_template is None:

            return JsonResponse({'reason': "form not found"}, status=400)
#            return HttpResponseBadRequest("ФОРМА НЕ НАЙДЕНА")

#        print(current_template['name'])      ## вывод имени наиболее подходящщей формы

        format_fields = []
        for field_name, field_type in current_template.items():
            if field_name == 'name':
                continue
            input_value = query_post[field_name]
            if field_type == 'date':

                pattern = r'(?<!\d)(?:0?[1-9]|[12][0-9]|3[01]).(?:0?[1-9]|1[0-2]).(?:21[0-9][0-9]|20[01][0-9])(?!\d)'
                pattern1 = r'(?<!\d)(?:21[0-9][0-9]|20[01][0-9])-(?:0?[1-9]|1[0-2])-(?:0?[1-9]|[12][0-9]|3[01])(?!\d)'
                result = bool(re.findall(pattern, input_value))
                result1 = bool(re.findall(pattern1, input_value))
                if result is True or result1 is True:
#                    print("формат данных соответствует заданному: =", "дата")
                    continue
                else:
#                    print("некорректный формат данных  для поля date input_value = ", input_value )
                    format_date = (field_name, field_type)
                    format_fields.append(format_date)

            input_value = query_post[field_name]
            if field_type == 'phone':

                pattern = re.compile(r"(\+7)[\s]\d{3}[\s]\d{3}[\s]\d{2}[\s]\d{2}$")
                result = bool (re.search(pattern, input_value))
                if result is True:
#                    print("формат данных соответствует заданному: =", "номер телефона")
                    continue
                else:
#                    print("некорректный формат данных для поля phone input_value = ", input_value)
                    format_phone = (field_name, field_type)
                    format_fields.append(format_phone)

            input_value = query_post[field_name]
            if field_type == 'email':
                pattern = r"^[-\w\.]+@([-\w]+\.)+[-\w]{2,4}$"
                result = bool(re.findall(pattern, input_value))
                if result is True:
#                    print("формат данных соответствует заданному: =", "адрес электронной почты")
                    continue
                else:
#                    print("некорректный формат данных для поля email input_value = ", input_value)
                    format_email = (field_name, field_type)
                    format_fields.append(format_email)

            # else:
#                field_name = str(field_name)
#                field_type = str(field_type)
#                print({field_name + ':' + field_type})

        dict_bad_format = dict(format_fields)
        list_correct_form = [("name_form_template", current_template['name'])]
        dict_good_form = dict(list_correct_form)

#        print(dict_bad_format)

#        json_file = open('bad_format.json', 'w+', encoding='utf8')
#        json.dump(dict_bad_format, json_file)
#        json_file.close()
#        return HttpResponseBadRequest("некорректный формат данных ")

        if not dict_bad_format :

#            json_file1 = open('good_format.json', 'w+', encoding='utf8')
#            json.dump(dict_good_form, json_file1)
#            json_file1.close()
            return JsonResponse(dict_good_form)
        else:
            return JsonResponse(dict_bad_format, status=400)
#         return HttpResponseBadRequest("некорректный формат данных ")



    return HttpResponseRedirect("/")


