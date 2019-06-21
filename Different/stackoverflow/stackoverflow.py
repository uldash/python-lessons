def download_survey():
    import os
    import shutil
    import zipfile
    import requests

    request = requests.get(
        "https://drive.google.com/uc?export=download&id=1_9On2-nsBQIw3JiY43sWbrF8EjrqrR4U"
    )
    with open("survey2018.zip", "wb") as file:
        file.write(request.content)

    with zipfile.ZipFile('survey2018.zip') as zip:
        zip.extractall('survey2018')

    shutil.move('survey2018/survey_results_public.csv', 'mysurvey.csv')
    shutil.rmtree('survey2018')
    os.remove('survey2018.zip')


download_survey()

# TODO 2019.06.19: refactor this code!
