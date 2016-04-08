#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Adsb Rx
# Generated: Thu Apr  7 23:02:14 2016
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import osmosdr
import sip
import sys
import time


class adsb_rx(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Adsb Rx")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Adsb Rx")
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "adsb_rx")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.update_rate = update_rate = 60
        self.rf_gain = rf_gain = 0
        self.if_gain = if_gain = 16
        self.fs_mhz = fs_mhz = 8
        self.fc_mhz = fc_mhz = 1089
        self.bb_gain = bb_gain = 16

        ##################################################
        # Blocks
        ##################################################
        self._rf_gain_tool_bar = Qt.QToolBar(self)
        self._rf_gain_tool_bar.addWidget(Qt.QLabel("rf_gain"+": "))
        self._rf_gain_line_edit = Qt.QLineEdit(str(self.rf_gain))
        self._rf_gain_tool_bar.addWidget(self._rf_gain_line_edit)
        self._rf_gain_line_edit.returnPressed.connect(
        	lambda: self.set_rf_gain(eng_notation.str_to_num(str(self._rf_gain_line_edit.text().toAscii()))))
        self.top_layout.addWidget(self._rf_gain_tool_bar)
        self._if_gain_tool_bar = Qt.QToolBar(self)
        self._if_gain_tool_bar.addWidget(Qt.QLabel("if_gain"+": "))
        self._if_gain_line_edit = Qt.QLineEdit(str(self.if_gain))
        self._if_gain_tool_bar.addWidget(self._if_gain_line_edit)
        self._if_gain_line_edit.returnPressed.connect(
        	lambda: self.set_if_gain(eng_notation.str_to_num(str(self._if_gain_line_edit.text().toAscii()))))
        self.top_layout.addWidget(self._if_gain_tool_bar)
        self._fs_mhz_tool_bar = Qt.QToolBar(self)
        self._fs_mhz_tool_bar.addWidget(Qt.QLabel("fs_mhz"+": "))
        self._fs_mhz_line_edit = Qt.QLineEdit(str(self.fs_mhz))
        self._fs_mhz_tool_bar.addWidget(self._fs_mhz_line_edit)
        self._fs_mhz_line_edit.returnPressed.connect(
        	lambda: self.set_fs_mhz(eng_notation.str_to_num(str(self._fs_mhz_line_edit.text().toAscii()))))
        self.top_layout.addWidget(self._fs_mhz_tool_bar)
        self._fc_mhz_tool_bar = Qt.QToolBar(self)
        self._fc_mhz_tool_bar.addWidget(Qt.QLabel("fc_mhz"+": "))
        self._fc_mhz_line_edit = Qt.QLineEdit(str(self.fc_mhz))
        self._fc_mhz_tool_bar.addWidget(self._fc_mhz_line_edit)
        self._fc_mhz_line_edit.returnPressed.connect(
        	lambda: self.set_fc_mhz(eng_notation.str_to_num(str(self._fc_mhz_line_edit.text().toAscii()))))
        self.top_layout.addWidget(self._fc_mhz_tool_bar)
        self._bb_gain_tool_bar = Qt.QToolBar(self)
        self._bb_gain_tool_bar.addWidget(Qt.QLabel("bb_gain"+": "))
        self._bb_gain_line_edit = Qt.QLineEdit(str(self.bb_gain))
        self._bb_gain_tool_bar.addWidget(self._bb_gain_line_edit)
        self._bb_gain_line_edit.returnPressed.connect(
        	lambda: self.set_bb_gain(eng_notation.str_to_num(str(self._bb_gain_line_edit.text().toAscii()))))
        self.top_layout.addWidget(self._bb_gain_tool_bar)
        self.qtgui_sink_x_0 = qtgui.sink_c(
        	8192, #fftsize
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	fc_mhz*1e6, #fc
        	fs_mhz*1e6, #bw
        	"", #name
        	True, #plotfreq
        	True, #plotwaterfall
        	True, #plottime
        	True, #plotconst
        )
        self.qtgui_sink_x_0.set_update_time(1.0/update_rate)
        self._qtgui_sink_x_0_win = sip.wrapinstance(self.qtgui_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_sink_x_0_win)
        
        self.qtgui_sink_x_0.enable_rf_freq(True)
        
        
          
        self.osmosdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + "hackrf=0,bias=1" )
        self.osmosdr_source_0.set_sample_rate(fs_mhz*1e6)
        self.osmosdr_source_0.set_center_freq(fc_mhz*1e6, 0)
        self.osmosdr_source_0.set_freq_corr(0, 0)
        self.osmosdr_source_0.set_dc_offset_mode(0, 0)
        self.osmosdr_source_0.set_iq_balance_mode(0, 0)
        self.osmosdr_source_0.set_gain_mode(False, 0)
        self.osmosdr_source_0.set_gain(rf_gain, 0)
        self.osmosdr_source_0.set_if_gain(if_gain, 0)
        self.osmosdr_source_0.set_bb_gain(bb_gain, 0)
        self.osmosdr_source_0.set_antenna("", 0)
        self.osmosdr_source_0.set_bandwidth(0, 0)
          

        ##################################################
        # Connections
        ##################################################
        self.connect((self.osmosdr_source_0, 0), (self.qtgui_sink_x_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "adsb_rx")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()


    def get_update_rate(self):
        return self.update_rate

    def set_update_rate(self, update_rate):
        self.update_rate = update_rate

    def get_rf_gain(self):
        return self.rf_gain

    def set_rf_gain(self, rf_gain):
        self.rf_gain = rf_gain
        self.osmosdr_source_0.set_gain(self.rf_gain, 0)
        Qt.QMetaObject.invokeMethod(self._rf_gain_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.rf_gain)))

    def get_if_gain(self):
        return self.if_gain

    def set_if_gain(self, if_gain):
        self.if_gain = if_gain
        self.osmosdr_source_0.set_if_gain(self.if_gain, 0)
        Qt.QMetaObject.invokeMethod(self._if_gain_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.if_gain)))

    def get_fs_mhz(self):
        return self.fs_mhz

    def set_fs_mhz(self, fs_mhz):
        self.fs_mhz = fs_mhz
        self.osmosdr_source_0.set_sample_rate(self.fs_mhz*1e6)
        self.qtgui_sink_x_0.set_frequency_range(self.fc_mhz*1e6, self.fs_mhz*1e6)
        Qt.QMetaObject.invokeMethod(self._fs_mhz_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.fs_mhz)))

    def get_fc_mhz(self):
        return self.fc_mhz

    def set_fc_mhz(self, fc_mhz):
        self.fc_mhz = fc_mhz
        self.osmosdr_source_0.set_center_freq(self.fc_mhz*1e6, 0)
        self.qtgui_sink_x_0.set_frequency_range(self.fc_mhz*1e6, self.fs_mhz*1e6)
        Qt.QMetaObject.invokeMethod(self._fc_mhz_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.fc_mhz)))

    def get_bb_gain(self):
        return self.bb_gain

    def set_bb_gain(self, bb_gain):
        self.bb_gain = bb_gain
        self.osmosdr_source_0.set_bb_gain(self.bb_gain, 0)
        Qt.QMetaObject.invokeMethod(self._bb_gain_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.bb_gain)))


def main(top_block_cls=adsb_rx, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
