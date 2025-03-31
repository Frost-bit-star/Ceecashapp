from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.webview import WebView
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.sidebar import SideBar  # Ensure you have the sidebar module

class WebViewApp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="horizontal", **kwargs)

        # Sidebar for navigation
        self.sidebar = SideBar(size_hint=(0.3, 1))
        self.toggle_button = ToggleButton(text="Toggle Sidebar", size_hint=(1, 0.1), on_press=self.toggle_sidebar)
        self.sidebar.add_widget(self.toggle_button)

        register_btn = Button(text="Register", size_hint=(1, 0.1), on_press=self.open_register)
        self.sidebar.add_widget(register_btn)

        # WebView to display site
        self.webview = WebView(url="https://ceecash.wuaze.com/menu.php")

        # Adding Sidebar and WebView to Layout
        self.add_widget(self.sidebar)
        self.add_widget(self.webview)

    def toggle_sidebar(self, instance):
        if self.sidebar.width == 0:
            self.sidebar.width = self.sidebar.size_hint[0] * self.width
        else:
            self.sidebar.width = 0

    def open_register(self, instance):
        self.webview.url = "https://ceecash.wuaze.com/register.php"

class MyApp(App):
    def build(self):
        return WebViewApp()

if __name__ == "__main__":
    MyApp().run()
