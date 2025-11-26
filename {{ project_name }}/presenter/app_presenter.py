from views import AppView

class AppPresenter:
    def __init__(self,view : AppView):
        self._view = view
