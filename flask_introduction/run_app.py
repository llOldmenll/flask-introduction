import os

# from flask_introduction.library._01_simple import app
# from flask_introduction.library._02_html_inside_view import app
# from flask_introduction.library._03_template_str_inside_view import app
# from flask_introduction.library._04_template_outside_view import app
# from flask_introduction.library._05_basic_routing import app
# from flask_introduction.library._06_raising_custom_errors import app
# from flask_introduction.library._07_request_info import app
# from flask_introduction.library._08_redirects import app
# from flask_introduction.library._09_simple_database_app import app
# from flask_introduction.library._10_database_app_template_eng import app
# from flask_introduction.library._11_database_app_template_conditional import app
# from flask_introduction.library._12_database_app_with_join import app
# from flask_introduction.library._13_simple_form_submission import app
# from flask_introduction.library._14_static_files import app

from flask_introduction.library._15_template_inheritance import app

if __name__ == '__main__':
    app.debug = True
    host = os.environ.get('IP', '0.0.0.0')
    port = int(os.environ.get('PORT', 8080))
    app.run(host=host, port=port)
