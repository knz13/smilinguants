

class Watcher:
    watcher_list = []
    def __init__(self,value_to_watch,on_changed = None) -> None:
        self.__value = value_to_watch
        self.__old_value = value_to_watch
        self.__on_changed = on_changed
        Watcher.watcher_list.append(self)

    def update(self):
        if self.__value != self.__old_value:
            if callable(self.__on_changed):
                self.__on_changed()
    def __del__(self):
        Watcher.watcher_list.remove(self)