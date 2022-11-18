import os
from tkinter import *

from src.repository.repository import Repository
from src.service.service import Service
from src.ui.ui import UI


def get_absolute_path(relative_path):
    return os.path.join(os.path.dirname(__file__), relative_path)


if __name__ == "__main__":
    repository = Repository(get_absolute_path('data/employees.csv'), get_absolute_path('data/ratings.csv'))
    service = Service(repository)

    root = Tk()
    root.title('Employee rating tool')
    root.geometry('450x635')
    root.resizable(width=False, height=False)
    root.protocol("WM_DELETE_WINDOW", sys.exit)
    UI(root, service)
    root.mainloop()
