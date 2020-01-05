from PySide2.QtWidgets import *
from PySide2.QtCore import Qt
from utils import Screen

_LOW_LEAK = 20
_LOW_TEMPERATURE = 30
_LOW_DEPTH = 300
_LOW_ACCELERATION = 5
_CRITICAL_LEAK = 50
_CRITICAL_TEMPERATURE = 50
_CRITICAL_DEPTH = 500
_CRITICAL_ACCELERATION = 10
_ATTENTION_LEAK = 40;
_ATTENTION_TEMPERATURE = 30;
_ATTENTION_DEPTH = 20;
_ATTENTION_ACCELERATION = 20;


class ConnectionStatus(QWidget):

    def __init__(self, _connection_status_header: str, _connection_status_body=[], _connection_status_footer="",
                 _connection_color="", _low_limit: float = None, _high_limit: float = None,
                 _attention_limit: float = None, ):
        """

        :param _connection_status_header: The header for the connection status. This is where the user input the name
        :param _connection_status_body: An array of values for the body
        :param _connection_status_footer: An optional footer
        :param _connection_color: An optional color for the status they may like
        """
        super(ConnectionStatus, self).__init__()
        self._connection_status_header = _connection_status_header
        self._connection_status_body = _connection_status_body
        self._connection_status_footer = _connection_status_footer
        self._connection_color = _connection_color

        self._layout = QVBoxLayout()  # create a QVboxLayout for the frame
        self._layout_l = QGridLayout() # create a QVboxLayout for the frame
        self._connection_status_header_label = QLabel()  # create a label for the frame
        self._connection_status_footer_label = QLabel()


        self._layout.addWidget(self._connection_status_header_label)
        self._status_dict = {}  # A status dictionary to store all the status of the dictionary

        # makes a directory to connect a label to connection status.
        self._frame = QFrame();
        row = 0
        column = 0
        for x in self._connection_status_body:
            label = QLabel()
            self._status_dict[label] = x
            self._layout_l.addWidget(label, row , column)
            column += 1;
            if column > 1:
                column = 0
                row += 1

        self._frame.setLayout(self._layout_l)

        self._layout.addWidget(self._frame)
        self._layout.addWidget(self._connection_status_footer_label)


        self.setLayout(self._layout)  # then set the layout widget
        self._set_style()

    def _set_style(self):

        self._layout.setSpacing(0);

        for key, value in {self._connection_status_header_label: self._connection_status_header,
                           self._connection_status_footer_label: self._connection_status_footer}.items():
            key.setAlignment(Qt.AlignCenter)
            key.setText(value)

        for key, value in self._status_dict.items():
            key.setAlignment(Qt.AlignCenter)
            key.setText(value)
            key.setStyleSheet("font-size: 20px");

        self.setStyleSheet("""
              QWidget {   
                   font-family: Arial;
                   background-color: rgb(8, 64, 67);
               }
    
               QLabel {
                   color: white;
                    font-family: cursive
    
               }
               """)

        if self._connection_color:
            self._frame.setStyleSheet("""background-color: orange;
                                      border: none;""")
            self.setStyleSheet("""
                QLabel {
                   color: white;
                   font-family: cursive;
    
                    }
                QFrame {
                  border: 5px solid orange;

                }
                QWidget {   
                  font-family: Arial;
                  background-color: rgb(8, 64, 67);
                }
                """);
            for key, value in self._status_dict.items():
                key.setStyleSheet("""
                    background-color: orange;
                    font-size: 20px;
                """)



            def update_values(self):
                pass


class ConnectionStatusSample(Screen):
    '''
    This is a screen which is going to repersent the status of the raseberry pi
    '''

    def __init__(self):
        super().__init__()

        self._leak_sensor = ConnectionStatus("Leak Sensor", ["50"])
        self._temperature = ConnectionStatus("Temperature", ["50"])
        self._depth = ConnectionStatus("Depth", ["50"])
        self._acceleration = ConnectionStatus("Acceleration", ["50", "70", "90", "50"])
        self._raspberry_pi = ConnectionStatus("R Pi", ["Fake Status"], "Arduino", "orange")
        self._land = ConnectionStatus("LAND", ["Fake Status"], "R Pi", "orange")

    def _config(self):
        self._layout = QHBoxLayout()
        self._layout.addWidget(self._leak_sensor)
        self._layout.addWidget(self._temperature)
        self._layout.addWidget(self._depth)
        self._layout.addWidget(self._acceleration)
        self._layout.addWidget(self._raspberry_pi)
        self._layout.addWidget(self._land)
        self.setLayout(self._layout)


if __name__ == "__main__":
    app = QApplication()
    form = ConnectionStatusSample()
    form._config()
    form.show()
    app.exec_()
