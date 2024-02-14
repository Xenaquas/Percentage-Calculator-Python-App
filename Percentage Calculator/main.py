from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.core.window import Window

Builder.load_string("""
<Calculator@AnchorLayout>:
    orientation: 'vertical'
    anchor_x: 'center'
    anchor_y: 'center'
    padding: 10
    spacing: 10

    BoxLayout:
        orientation: 'horizontal'
        size_hint_y: None
        height: '40dp'
        Label:
            text: 'Total Marks:        '
            size_hint_x: None
            width: self.texture_size[0]
        TextInput:
            id: total_marks_input
            hint_text: 'Enter Total Marks'
            input_filter: 'float'

    BoxLayout:
        orientation: 'horizontal'
        size_hint_y: None
        height: '40dp'
        Label:
            text: 'Marks Obtained:  '
            size_hint_x: None
            width: self.texture_size[0]
        TextInput:
            id: marks_obtained_input
            hint_text: 'Enter Marks Obtained'
            input_filter: 'float'

    Button:
        text: 'Calculate'
        size_hint_y: None
        height: 50
        on_press: root.calculate_percentage()

    Label:
        id: result_label
        text: 'Percentage: '
""")


class Calculator(BoxLayout):

    def calculate_percentage(self):
        total_marks = self.ids.total_marks_input.text
        marks_obtained = self.ids.marks_obtained_input.text

        # Check if the fields are empty or not
        if not total_marks or not marks_obtained:
            self.ids.result_label.text = 'Please fill in both fields!'
            return

        # Convert to float and calculate
        total_marks = float(total_marks)
        marks_obtained = float(marks_obtained)

        # Check if total marks is non-zero
        if total_marks == 0:
            self.ids.result_label.text = 'Total Marks cannot be zero!'
            return

        percentage = (marks_obtained / total_marks) * 100
        self.ids.result_label.text = f'Percentage: {percentage:.2f}%'


class PercentageCalculatorApp(App):

    def build(self):
        # Set the window size to match a typical Android smartphone login screen size
        Window.size = (360, 640)
        return Calculator()


if __name__ == '__main__':
    PercentageCalculatorApp().run()
