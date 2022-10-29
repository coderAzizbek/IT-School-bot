from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from keyboards.inline.callback_data import course_data


course=InlineKeyboardMarkup(row_width=1)
python=InlineKeyboardButton(text="Kampyuter Savodxonlik",callback_data=course_data.new(item_name="komp_course"))
course.insert(python)
python=InlineKeyboardButton(text="🐍 Python dasturlash asoslari",callback_data=course_data.new(item_name="python_course"))
course.insert(python)
python=InlineKeyboardButton(text="Griafik Dizayner",callback_data=course_data.new(item_name="grafik_course"))
course.insert(python)
python=InlineKeyboardButton(text="Web Dasturlash",callback_data=course_data.new(item_name="web_course"))
course.insert(python)
python=InlineKeyboardButton(text="Android dasturlash",callback_data=course_data.new(item_name="Android_course"))
course.insert(python)
python=InlineKeyboardButton(text="Robot texnika",callback_data=course_data.new(item_name="robot_course"))
course.insert(python)
python=InlineKeyboardButton(text="orqaga",callback_data=course_data.new(item_name="cancel"))
course.insert(python)



# course = {
#     "Kampyuter Savodxonlik": "komp_course",
#     "Python dasturlash asoslari":"python_course",
#     "Griafik Dizayner": "grafik_course",
#     "Web Dasturlash": "web_course",
#     "Android dasturlash": "Android_course",
#     "Robot texnika": "robot_course",
#     "Orqaga":"cansel",
#
# }
#
# CourseMenu=InlineKeyboardMarkup(row_width=1)
# for key,value in course.items():
#     CourseMenu.insert(InlineKeyboardButton(text=key,callback_data=course_data.new(item_name=value)))

