#! python3

import re
# This function finds numbers that have 2 digits in the area code
def numeros_bsas():
    telefonos_cod2d = re.compile(r'''(
    ((\d)?(\d\d)|\((\d)?\d\d\)) #Codigo de área Caba, Gba y Bs As provincia
    (\s|-)?                    #primer guion
    ((\d\d\d\d)                  #primeros 4 digitos
    (\s|-)?                     #segundo guion
    (\d\d\d\d))(,)?                      #segundos 4 digitos
    )
    ''', re.VERBOSE)  # Regex
    match_ca2d = telefonos_cod2d.findall(texto)         # Match object
    datos_ca2d = []
    for match in match_ca2d:
        datos_ca2d.append(match[0])
    return datos_ca2d

# This function finds numbers that have 3 digits in the area code
def numeros_area_cod_3d():
    telefonos_cod3d = re.compile(r'''(
    ((\d)?(\d\d\d)|\((\d)?\d\d\d\)) #Codigo de área de 3 dígitos
    (\s|-)?                    #primer guion
    (\d\d\d)                  #primeros 3 digitos
    (\s|-)?                      #segundo guion
    (\d\d\d\d)(,)?                      #segundos 4 digitos
    )
    ''', re.VERBOSE)
    match_ca3d = telefonos_cod3d.findall(texto)
    datos_ca3d = []
    for match in match_ca3d:
        datos_ca3d.append(match[0])
    return datos_ca3d

# This function finds numbers that have 4 digits in the area code
def numeros_area_cod_4d():
    telefonos_cod4d = re.compile(r'''(
    ((\d)?(\d\d\d\d)|\((\d)?\d\d\d\d\)) #Codigo de área de 3 dígitos
    (\s|-)?                    #primer guion
    (\d\d)                  #primeros 3 digitos
    (\s|-)?                     #segundo guion
    (\d\d\d\d)(,)?                      #segundos 4 digitos
    )
    ''', re.VERBOSE)
    match_ca4d = telefonos_cod4d.findall(texto)
    datos_ca4d = []
    for match in match_ca4d:
        datos_ca4d.append(match[0])
    return datos_ca4d

# This function finds email addresses
def email_founder():
    mail_regex = re.compile(r'''
    ([a-zA-Z0-9()<>:,;@"!#$%&'*+/=?^_`{}|~.]+   # First part
    @                                           # @ Symbol
    ([a-zA-Z0-9()<>:,;@"!#$%&'*+/=?^_`{}|~.])*)   # Domain
''', re.VERBOSE)
    mailsextr = mail_regex.findall(emailData)
    e_mails = []
    for email in mailsextr:
        e_mails.append(email[0])
    return e_mails


texto = 'Llamame al (11)-6499-7284, o al (011) 1111-1111, o al 1234-1234 en 2020. Si estoy en Rosario, entomces ' \
        'llamame al (341)-213-4763, O EN aRRECIFES AL 2478-45-2480'

emailData = 'Unidad Funcional de Instrucción y Juicio de Vicente López Este:  ufij.vle.si@mpba.gov.ar ' \
            'Unidad Funcional de Instrucción y Juicio de Vicente López Oeste: ufij.vlo.si@mpba.gov.ar' \
            'Unidad Funcional de Instrucción y Juicio de Violencia de Género Vicente López: ' \
            'ufij.genero.vl.si@mpba.gov.ar'

pn_2d_results = '\n'.join(numeros_bsas())
pn_3d_results = '\n'.join(numeros_area_cod_3d())
pn_4d_results = '\n'.join(numeros_area_cod_4d())
email_results = '\n'.join(email_founder())
print(pn_2d_results)
print(pn_3d_results)
print(pn_4d_results)
print(email_results)
