from PySide6 import QtCore


def action_menu_bar(main_window):
    left_body_frame = main_window.ui.left_bodyframe
    width = left_body_frame.width()
    if width == 215:
        new_width = 2
    else:
        new_width = 215
    main_window.animation = QtCore.QPropertyAnimation(
        left_body_frame, b"maximumWidth"
    )
    main_window.animation.setDuration(200)
    main_window.animation.setStartValue(width)
    main_window.animation.setEndValue(new_width)
    main_window.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
    main_window.animation.start()
