from file_monitor import FileMonitor


if __name__ == "__main__":
    path = input("Folder to monitor: ")

    monitor = FileMonitor(path)
    monitor.start()