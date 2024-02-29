from django.utils.text import slugify


class Generate():
    

    def _generate_whats_number(phone, phone_is_whats):
        if not phone_is_whats: return ""
        clear_number = ''.join(filter(str.isdigit, phone))
        whats_number = "55" + clear_number
        return whats_number


    def _generate_social_links(links):
        dictn = {}
        for link in links:
            if 'facebook' in link:
                dictn['facebook'] = link
            elif 'instagram' in link:
                dictn['instagram'] = link                
        return dictn
    

    def _generate_url(company_name, company_address):
         return f'{slugify(company_address).split("-")[-2].lower()}/{slugify(company_name)}'