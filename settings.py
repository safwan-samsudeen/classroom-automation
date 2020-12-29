""" Settings for automation process """

from secrets import EMAIL_ADDRESS, PASSWORD
BASE_URL = 'https://classroom.google.com/u/0/'


class Settings():
    """ A class for handling settings and configaration """

    def __init__(self):
        self.email_address = EMAIL_ADDRESS
        self.password = PASSWORD
        self.max_wait_time = 10
        self.scroll_pause_time = 1.5
        self.base_url = BASE_URL
        self.headless = True
        self.student_classes_href = [
            'https://classroom.google.com/u/0/c/MTA3MjQ1ODYwODcw'
        ]
        self.defaults = [
            'Al Qamar Academy',
            'Aneesa Jamal',
        ]
        self.selector_mapping = {
            'email_input': 'input[type="email"]',
            'password_input': 'input[type="password"]',
            'class_links_selector': 'a.onkcGd.kj3hr.YVvGBb',
            'videos': '.jrhqBd.LBlAUc.Aopndd.ZoT1D.TIunU',
            'video_link': '.uqZtlf.x0HGk.QRiHXd.MymH0d.maXJsd',
            'answers_selector': '.hYt5f.FRDm8d > .WkZsyc',
            'username': '.Evt7cb.UmiGNb',
            'date': '.IMvYId.zQwDwf',
                    'answer': '.NjE5zd',
            'student_answers_link': '.GOm7re.QRiHXd > div a',
            'teacher_answers_link': '.kpDQ8.yHjGtf.maXJsd.MymH0d',
            'work_link': 'a[guidedhelpid="classworkTab"]',
            'video_panel_link': 'a[aria-label="Weekly Video"]'
        }
        self.people_data = {
            'Abdullah Ibrahim': ['Male', 8],
            'Abdullah Khalifatullah': ['Male', 8],
            'Abdul Majid Syed': ['Male', 8],
            'Afnan Ahmed': ['Male', 8],
            'Anam Fathima': ['Female', 8],
            'Fareeha Rafeeq': ['Female', 8],
            'Hasna Jabir': ['Female', 8],
            'Ishaal Azeez': ['Female', 8],
            'Safwan Samsudeen': ['Male', 8],
            'Shahana Shameer': ['Female', 8],
            'Muhammad Shakeel': ['Male', 8],
            'Rayya Shawar': ['Female', 8],
            'Tasneem Kausar': ['Female', 8],
            'Mansoor Ahmed': ['Male', 6],
            'Muhammad Ashfaque': ['Male', 6],
            'Fawziya Fawziya': ['Female', 6],
            'Muhammed Hammad': ['Male', 6],
            'Hamdan Jabir': ['Male', 6],
            'Hajira Raafiya': ['Female', 6],
            'Luqmaan Safee': ['Male', 6],
            'Abdul Muiz Syed': ['Male', 6],
            'Zoya Taher': ['Female', 6],
        }
