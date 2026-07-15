from observers.student_observer import StudentObserver

class ClassroomNoticeBoard:

    def __init__(self):
        self.observers = []

    def attach(self, observer):

        self.observers.append(observer)

    def detach(self, observer):

        self.observers.remove(observer)

    def notify(self, notice):

        for observer in self.observers:
            observer.update(notice)

    def post_notice(self, notice):

        self.notify(notice)