import abc


# region Product

# region Button
class Button(abc.ABC):

    @abc.abstractmethod
    def get_color(self):
        pass

    def on_click(self):
        print('Click!')


class BlackButton(Button):
    def get_color(self):
        return '#293133'


class WhiteButton(Button):
    def get_color(self):
        return '#E8E8E8'
# endregion


# region Checkbox
class Checkbox(abc.ABC):

    @abc.abstractmethod
    def get_color(self):
        pass

    def is_active(self):
        print('Checkbox is active')


class BlackCheckbox(Checkbox):
    def get_color(self):
        return '#0098A3'


class WhiteCheckbox(Checkbox):
    def get_color(self):
        return '#B8F9FF'
# endregion

# endregion


# region Creator
class GUICreator(abc.ABC):

    @abc.abstractmethod
    def create_button(self) -> Button:
        pass

    @abc.abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass


class BlackThemeCreator(GUICreator):
    def create_button(self):
        return BlackButton()

    def create_checkbox(self):
        return BlackCheckbox()


class WhiteThemeCreator(GUICreator):
    def create_button(self):
        return WhiteButton()

    def create_checkbox(self):
        return WhiteCheckbox()

# endregion


# region Application
class Application:
    def __init__(self, factory):
        self.factory = factory

    def create_button(self):
        return self.factory.create_button()

    def create_checkbox(self):
        return self.factory.create_checkbox()

    def get_theme_info(self):
        button = self.create_button()
        checkbox = self.create_checkbox()
        print(f'button: {button.get_color()}, checkbox: {checkbox.get_color()}')
        return
# endregion


# region example
if __name__ == '__main__':
    theme_factories = {
        'black': BlackThemeCreator,
        'white': WhiteThemeCreator,
    }

    black_theme = theme_factories['black']()
    white_theme = theme_factories['white']()

    app = Application(black_theme)
    app.get_theme_info()

    app = Application(white_theme)
    app.get_theme_info()

    '''
        button: #293133, checkbox: #0098A3
        button: #E8E8E8, checkbox: #B8F9FF
    '''
# endregion
