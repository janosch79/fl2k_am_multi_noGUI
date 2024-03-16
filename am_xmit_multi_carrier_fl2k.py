#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Am Xmit Multi Carrier Fl2K
# GNU Radio version: 3.10.1.1

from gnuradio import analog
from gnuradio import blocks
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import network




class am_xmit_multi_carrier_fl2k(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Am Xmit Multi Carrier Fl2K", catch_exceptions=True)

        ##################################################
        # Variables
        ##################################################
        self.rf_sample_rate = rf_sample_rate = 2048e3
        self.af_sample_rate = af_sample_rate = 22e3
        self.start_rf = start_rf = 0e3
        self.fir_interp = fir_interp = (int)(rf_sample_rate/af_sample_rate)
        self.fgain = fgain = 250

        ##################################################
        # Blocks
        ##################################################
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=4,
                decimation=1,
                taps=[],
                fractional_bw=0)
        self.network_udp_source_0_1 = network.udp_source(gr.sizeof_float, 1, 2609, 0, 1472, False, False, False)
        self.network_udp_source_0_0_0_0_0_0_0_0_2 = network.udp_source(gr.sizeof_float, 1, 2611, 0, 1472, False, False, False)
        self.network_udp_source_0_0_0_0_0_0_0_0_1_1 = network.udp_source(gr.sizeof_float, 1, 2614, 0, 1472, False, False, False)
        self.network_udp_source_0_0_0_0_0_0_0_0_1_0 = network.udp_source(gr.sizeof_float, 1, 2610, 0, 1472, False, False, False)
        self.network_udp_source_0_0_0_0_0_0_0_0_1 = network.udp_source(gr.sizeof_float, 1, 2613, 0, 1472, False, False, False)
        self.network_udp_source_0_0_0_0_0_0_0_0_0 = network.udp_source(gr.sizeof_float, 1, 2612, 0, 1472, False, False, False)
        self.network_udp_source_0_0_0_0_0_0_0_0 = network.udp_source(gr.sizeof_float, 1, 2608, 0, 1472, False, False, False)
        self.network_udp_source_0_0_0_0_0_0_0 = network.udp_source(gr.sizeof_float, 1, 2607, 0, 1472, False, False, False)
        self.network_udp_source_0_0_0_0_0_0 = network.udp_source(gr.sizeof_float, 1, 2606, 0, 1472, False, False, False)
        self.network_udp_source_0_0_0_0_0 = network.udp_source(gr.sizeof_float, 1, 2605, 0, 1472, False, False, False)
        self.network_udp_source_0_0_0_0 = network.udp_source(gr.sizeof_float, 1, 2604, 0, 1472, False, False, False)
        self.network_udp_source_0_0_0 = network.udp_source(gr.sizeof_float, 1, 2603, 0, 1472, False, False, False)
        self.network_udp_source_0_0 = network.udp_source(gr.sizeof_float, 1, 2602, 0, 1472, False, False, False)
        self.network_udp_source_0 = network.udp_source(gr.sizeof_float, 1, 2601, 0, 1472, False, False, False)
        self.network_tcp_sink_0 = network.tcp_sink(gr.sizeof_char, 1, '127.0.0.1', 25000,2)
        self.low_pass_filter_5_1_0_2 = filter.interp_fir_filter_fff(
            fir_interp,
            firdes.low_pass(
                fgain,
                rf_sample_rate,
                8e3,
                4e3,
                window.WIN_HAMMING,
                6.76))
        self.low_pass_filter_5_1_0_1_1 = filter.interp_fir_filter_fff(
            fir_interp,
            firdes.low_pass(
                fgain,
                rf_sample_rate,
                8e3,
                4e3,
                window.WIN_HAMMING,
                6.76))
        self.low_pass_filter_5_1_0_1_0 = filter.interp_fir_filter_fff(
            fir_interp,
            firdes.low_pass(
                fgain,
                rf_sample_rate,
                8e3,
                4e3,
                window.WIN_HAMMING,
                6.76))
        self.low_pass_filter_5_1_0_1 = filter.interp_fir_filter_fff(
            fir_interp,
            firdes.low_pass(
                fgain,
                rf_sample_rate,
                8e3,
                4e3,
                window.WIN_HAMMING,
                6.76))
        self.low_pass_filter_5_1_0_0 = filter.interp_fir_filter_fff(
            fir_interp,
            firdes.low_pass(
                fgain,
                rf_sample_rate,
                8e3,
                4e3,
                window.WIN_HAMMING,
                6.76))
        self.low_pass_filter_5_1_0 = filter.interp_fir_filter_fff(
            fir_interp,
            firdes.low_pass(
                fgain,
                rf_sample_rate,
                8e3,
                4e3,
                window.WIN_HAMMING,
                6.76))
        self.low_pass_filter_5_1 = filter.interp_fir_filter_fff(
            fir_interp,
            firdes.low_pass(
                fgain,
                rf_sample_rate,
                8e3,
                4e3,
                window.WIN_HAMMING,
                6.76))
        self.low_pass_filter_5_0 = filter.interp_fir_filter_fff(
            fir_interp,
            firdes.low_pass(
                fgain,
                rf_sample_rate,
                8e3,
                4e3,
                window.WIN_HAMMING,
                6.76))
        self.low_pass_filter_5 = filter.interp_fir_filter_fff(
            fir_interp,
            firdes.low_pass(
                fgain,
                rf_sample_rate,
                8e3,
                4e3,
                window.WIN_HAMMING,
                6.76))
        self.low_pass_filter_4 = filter.interp_fir_filter_fff(
            fir_interp,
            firdes.low_pass(
                fgain,
                rf_sample_rate,
                8e3,
                4e3,
                window.WIN_HAMMING,
                6.76))
        self.low_pass_filter_3 = filter.interp_fir_filter_fff(
            fir_interp,
            firdes.low_pass(
                fgain,
                rf_sample_rate,
                8e3,
                4e3,
                window.WIN_HAMMING,
                6.76))
        self.low_pass_filter_2 = filter.interp_fir_filter_fff(
            fir_interp,
            firdes.low_pass(
                fgain,
                rf_sample_rate,
                8e3,
                4e3,
                window.WIN_HAMMING,
                6.76))
        self.low_pass_filter_1 = filter.interp_fir_filter_fff(
            fir_interp,
            firdes.low_pass(
                fgain,
                rf_sample_rate,
                8e3,
                4e3,
                window.WIN_HAMMING,
                6.76))
        self.low_pass_filter_0 = filter.interp_fir_filter_fff(
            fir_interp,
            firdes.low_pass(
                fgain,
                rf_sample_rate,
                8e3,
                4e3,
                window.WIN_HAMMING,
                6.76))
        self.blocks_multiply_xx_6 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_5_1_0_2 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_5_1_0_1_1 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_5_1_0_1_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_5_1_0_1 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_5_1_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_5_1_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_5_1 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_5_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_5 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_4 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_3 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_2 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_1 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_multiply_const_vxx_6 = blocks.multiply_const_ff(0.15)
        self.blocks_float_to_char_0 = blocks.float_to_char(1, 128)
        self.blocks_add_xx_2 = blocks.add_vff(1)
        self.blocks_add_xx_1_1 = blocks.add_vff(1)
        self.blocks_add_xx_1_0 = blocks.add_vff(1)
        self.blocks_add_xx_1 = blocks.add_vff(1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.blocks_add_const_vxx_5_1_0_2 = blocks.add_const_ff(1)
        self.blocks_add_const_vxx_5_1_0_1_1 = blocks.add_const_ff(1)
        self.blocks_add_const_vxx_5_1_0_1_0 = blocks.add_const_ff(1)
        self.blocks_add_const_vxx_5_1_0_1 = blocks.add_const_ff(1)
        self.blocks_add_const_vxx_5_1_0_0 = blocks.add_const_ff(1)
        self.blocks_add_const_vxx_5_1_0 = blocks.add_const_ff(1)
        self.blocks_add_const_vxx_5_1 = blocks.add_const_ff(1)
        self.blocks_add_const_vxx_5_0 = blocks.add_const_ff(1)
        self.blocks_add_const_vxx_5 = blocks.add_const_ff(1)
        self.blocks_add_const_vxx_4 = blocks.add_const_ff(1)
        self.blocks_add_const_vxx_3 = blocks.add_const_ff(1)
        self.blocks_add_const_vxx_2 = blocks.add_const_ff(1)
        self.blocks_add_const_vxx_1 = blocks.add_const_ff(1)
        self.blocks_add_const_vxx_0 = blocks.add_const_ff(1)
        self.analog_sig_source_x_5_1_0_2 = analog.sig_source_f(rf_sample_rate, analog.GR_SIN_WAVE, start_rf+(10*90e3), 1, 0, 0)
        self.analog_sig_source_x_5_1_0_1_1 = analog.sig_source_f(rf_sample_rate, analog.GR_SIN_WAVE, start_rf+(10*90e3)+(3*45e3), 1, 0, 0)
        self.analog_sig_source_x_5_1_0_1_0 = analog.sig_source_f(rf_sample_rate, analog.GR_SIN_WAVE, start_rf+(9*90e3), 1, 0, 0)
        self.analog_sig_source_x_5_1_0_1 = analog.sig_source_f(rf_sample_rate, analog.GR_SIN_WAVE, start_rf+(10*90e3)+(2*45e3), 1, 0, 0)
        self.analog_sig_source_x_5_1_0_0 = analog.sig_source_f(rf_sample_rate, analog.GR_SIN_WAVE, start_rf+(10*90e3)+(1*45e3), 1, 0, 0)
        self.analog_sig_source_x_5_1_0 = analog.sig_source_f(rf_sample_rate, analog.GR_SIN_WAVE, start_rf+(8*90e3), 1, 0, 0)
        self.analog_sig_source_x_5_1 = analog.sig_source_f(rf_sample_rate, analog.GR_SIN_WAVE, start_rf+(7*90e3), 1, 0, 0)
        self.analog_sig_source_x_5_0 = analog.sig_source_f(rf_sample_rate, analog.GR_SIN_WAVE, start_rf+(6*90e3), 1, 0, 0)
        self.analog_sig_source_x_5 = analog.sig_source_f(rf_sample_rate, analog.GR_SIN_WAVE, start_rf+(5*90e3), 1, 0, 0)
        self.analog_sig_source_x_4 = analog.sig_source_f(rf_sample_rate, analog.GR_COS_WAVE, start_rf+(4*90e3), 1, 0, 0)
        self.analog_sig_source_x_3 = analog.sig_source_f(rf_sample_rate, analog.GR_SIN_WAVE, start_rf+(3*90e3), 1, 0, 0)
        self.analog_sig_source_x_2 = analog.sig_source_f(rf_sample_rate, analog.GR_COS_WAVE, start_rf+(2*90e3), 1, 0, 0)
        self.analog_sig_source_x_1_0 = analog.sig_source_f(rf_sample_rate*4, analog.GR_SIN_WAVE, 531e3, 1, 0, 0)
        self.analog_sig_source_x_1 = analog.sig_source_f(rf_sample_rate, analog.GR_SIN_WAVE, start_rf+90e3, 1, 0, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(rf_sample_rate, analog.GR_COS_WAVE, start_rf+1, 1, 0, 0)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.analog_sig_source_x_1, 0), (self.blocks_multiply_xx_1, 1))
        self.connect((self.analog_sig_source_x_1_0, 0), (self.blocks_multiply_xx_6, 1))
        self.connect((self.analog_sig_source_x_2, 0), (self.blocks_multiply_xx_2, 1))
        self.connect((self.analog_sig_source_x_3, 0), (self.blocks_multiply_xx_3, 1))
        self.connect((self.analog_sig_source_x_4, 0), (self.blocks_multiply_xx_4, 1))
        self.connect((self.analog_sig_source_x_5, 0), (self.blocks_multiply_xx_5, 1))
        self.connect((self.analog_sig_source_x_5_0, 0), (self.blocks_multiply_xx_5_0, 1))
        self.connect((self.analog_sig_source_x_5_1, 0), (self.blocks_multiply_xx_5_1, 1))
        self.connect((self.analog_sig_source_x_5_1_0, 0), (self.blocks_multiply_xx_5_1_0, 1))
        self.connect((self.analog_sig_source_x_5_1_0_0, 0), (self.blocks_multiply_xx_5_1_0_0, 1))
        self.connect((self.analog_sig_source_x_5_1_0_1, 0), (self.blocks_multiply_xx_5_1_0_1, 1))
        self.connect((self.analog_sig_source_x_5_1_0_1_0, 0), (self.blocks_multiply_xx_5_1_0_1_0, 1))
        self.connect((self.analog_sig_source_x_5_1_0_1_1, 0), (self.blocks_multiply_xx_5_1_0_1_1, 1))
        self.connect((self.analog_sig_source_x_5_1_0_2, 0), (self.blocks_multiply_xx_5_1_0_2, 1))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_add_const_vxx_1, 0), (self.blocks_multiply_xx_1, 0))
        self.connect((self.blocks_add_const_vxx_2, 0), (self.blocks_multiply_xx_2, 0))
        self.connect((self.blocks_add_const_vxx_3, 0), (self.blocks_multiply_xx_3, 0))
        self.connect((self.blocks_add_const_vxx_4, 0), (self.blocks_multiply_xx_4, 0))
        self.connect((self.blocks_add_const_vxx_5, 0), (self.blocks_multiply_xx_5, 0))
        self.connect((self.blocks_add_const_vxx_5_0, 0), (self.blocks_multiply_xx_5_0, 0))
        self.connect((self.blocks_add_const_vxx_5_1, 0), (self.blocks_multiply_xx_5_1, 0))
        self.connect((self.blocks_add_const_vxx_5_1_0, 0), (self.blocks_multiply_xx_5_1_0, 0))
        self.connect((self.blocks_add_const_vxx_5_1_0_0, 0), (self.blocks_multiply_xx_5_1_0_0, 0))
        self.connect((self.blocks_add_const_vxx_5_1_0_1, 0), (self.blocks_multiply_xx_5_1_0_1, 0))
        self.connect((self.blocks_add_const_vxx_5_1_0_1_0, 0), (self.blocks_multiply_xx_5_1_0_1_0, 0))
        self.connect((self.blocks_add_const_vxx_5_1_0_1_1, 0), (self.blocks_multiply_xx_5_1_0_1_1, 0))
        self.connect((self.blocks_add_const_vxx_5_1_0_2, 0), (self.blocks_multiply_xx_5_1_0_2, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_add_xx_2, 0))
        self.connect((self.blocks_add_xx_1, 0), (self.blocks_add_xx_2, 1))
        self.connect((self.blocks_add_xx_1_0, 0), (self.blocks_add_xx_2, 3))
        self.connect((self.blocks_add_xx_1_1, 0), (self.blocks_add_xx_2, 2))
        self.connect((self.blocks_add_xx_2, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.blocks_float_to_char_0, 0), (self.network_tcp_sink_0, 0))
        self.connect((self.blocks_multiply_const_vxx_6, 0), (self.blocks_float_to_char_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_multiply_xx_1, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_multiply_xx_2, 0), (self.blocks_add_xx_0, 2))
        self.connect((self.blocks_multiply_xx_3, 0), (self.blocks_add_xx_0, 3))
        self.connect((self.blocks_multiply_xx_4, 0), (self.blocks_add_xx_1, 0))
        self.connect((self.blocks_multiply_xx_5, 0), (self.blocks_add_xx_1, 1))
        self.connect((self.blocks_multiply_xx_5_0, 0), (self.blocks_add_xx_1, 2))
        self.connect((self.blocks_multiply_xx_5_1, 0), (self.blocks_add_xx_1_1, 0))
        self.connect((self.blocks_multiply_xx_5_1_0, 0), (self.blocks_add_xx_1_1, 1))
        self.connect((self.blocks_multiply_xx_5_1_0_0, 0), (self.blocks_add_xx_1_0, 1))
        self.connect((self.blocks_multiply_xx_5_1_0_1, 0), (self.blocks_add_xx_1_0, 2))
        self.connect((self.blocks_multiply_xx_5_1_0_1_0, 0), (self.blocks_add_xx_1_1, 2))
        self.connect((self.blocks_multiply_xx_5_1_0_1_1, 0), (self.blocks_add_xx_1_0, 3))
        self.connect((self.blocks_multiply_xx_5_1_0_2, 0), (self.blocks_add_xx_1_0, 0))
        self.connect((self.blocks_multiply_xx_6, 0), (self.blocks_multiply_const_vxx_6, 0))
        self.connect((self.low_pass_filter_0, 0), (self.blocks_add_const_vxx_0, 0))
        self.connect((self.low_pass_filter_1, 0), (self.blocks_add_const_vxx_1, 0))
        self.connect((self.low_pass_filter_2, 0), (self.blocks_add_const_vxx_2, 0))
        self.connect((self.low_pass_filter_3, 0), (self.blocks_add_const_vxx_3, 0))
        self.connect((self.low_pass_filter_4, 0), (self.blocks_add_const_vxx_4, 0))
        self.connect((self.low_pass_filter_5, 0), (self.blocks_add_const_vxx_5, 0))
        self.connect((self.low_pass_filter_5_0, 0), (self.blocks_add_const_vxx_5_0, 0))
        self.connect((self.low_pass_filter_5_1, 0), (self.blocks_add_const_vxx_5_1, 0))
        self.connect((self.low_pass_filter_5_1_0, 0), (self.blocks_add_const_vxx_5_1_0, 0))
        self.connect((self.low_pass_filter_5_1_0_0, 0), (self.blocks_add_const_vxx_5_1_0_0, 0))
        self.connect((self.low_pass_filter_5_1_0_1, 0), (self.blocks_add_const_vxx_5_1_0_1, 0))
        self.connect((self.low_pass_filter_5_1_0_1_0, 0), (self.blocks_add_const_vxx_5_1_0_1_0, 0))
        self.connect((self.low_pass_filter_5_1_0_1_1, 0), (self.blocks_add_const_vxx_5_1_0_1_1, 0))
        self.connect((self.low_pass_filter_5_1_0_2, 0), (self.blocks_add_const_vxx_5_1_0_2, 0))
        self.connect((self.network_udp_source_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.network_udp_source_0_0, 0), (self.low_pass_filter_2, 0))
        self.connect((self.network_udp_source_0_0_0, 0), (self.low_pass_filter_3, 0))
        self.connect((self.network_udp_source_0_0_0_0, 0), (self.low_pass_filter_4, 0))
        self.connect((self.network_udp_source_0_0_0_0_0, 0), (self.low_pass_filter_5, 0))
        self.connect((self.network_udp_source_0_0_0_0_0_0, 0), (self.low_pass_filter_5_0, 0))
        self.connect((self.network_udp_source_0_0_0_0_0_0_0, 0), (self.low_pass_filter_5_1, 0))
        self.connect((self.network_udp_source_0_0_0_0_0_0_0_0, 0), (self.low_pass_filter_5_1_0, 0))
        self.connect((self.network_udp_source_0_0_0_0_0_0_0_0_0, 0), (self.low_pass_filter_5_1_0_0, 0))
        self.connect((self.network_udp_source_0_0_0_0_0_0_0_0_1, 0), (self.low_pass_filter_5_1_0_1, 0))
        self.connect((self.network_udp_source_0_0_0_0_0_0_0_0_1_0, 0), (self.low_pass_filter_5_1_0_1_0, 0))
        self.connect((self.network_udp_source_0_0_0_0_0_0_0_0_1_1, 0), (self.low_pass_filter_5_1_0_1_1, 0))
        self.connect((self.network_udp_source_0_0_0_0_0_0_0_0_2, 0), (self.low_pass_filter_5_1_0_2, 0))
        self.connect((self.network_udp_source_0_1, 0), (self.low_pass_filter_1, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_multiply_xx_6, 0))


    def get_rf_sample_rate(self):
        return self.rf_sample_rate

    def set_rf_sample_rate(self, rf_sample_rate):
        self.rf_sample_rate = rf_sample_rate
        self.set_fir_interp((int)(self.rf_sample_rate/self.af_sample_rate))
        self.analog_sig_source_x_0.set_sampling_freq(self.rf_sample_rate)
        self.analog_sig_source_x_1.set_sampling_freq(self.rf_sample_rate)
        self.analog_sig_source_x_1_0.set_sampling_freq(self.rf_sample_rate*4)
        self.analog_sig_source_x_2.set_sampling_freq(self.rf_sample_rate)
        self.analog_sig_source_x_3.set_sampling_freq(self.rf_sample_rate)
        self.analog_sig_source_x_4.set_sampling_freq(self.rf_sample_rate)
        self.analog_sig_source_x_5.set_sampling_freq(self.rf_sample_rate)
        self.analog_sig_source_x_5_0.set_sampling_freq(self.rf_sample_rate)
        self.analog_sig_source_x_5_1.set_sampling_freq(self.rf_sample_rate)
        self.analog_sig_source_x_5_1_0.set_sampling_freq(self.rf_sample_rate)
        self.analog_sig_source_x_5_1_0_0.set_sampling_freq(self.rf_sample_rate)
        self.analog_sig_source_x_5_1_0_1.set_sampling_freq(self.rf_sample_rate)
        self.analog_sig_source_x_5_1_0_1_0.set_sampling_freq(self.rf_sample_rate)
        self.analog_sig_source_x_5_1_0_1_1.set_sampling_freq(self.rf_sample_rate)
        self.analog_sig_source_x_5_1_0_2.set_sampling_freq(self.rf_sample_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(self.fgain, self.rf_sample_rate, 8e3, 4e3, window.WIN_HAMMING, 6.76))
        self.low_pass_filter_1.set_taps(firdes.low_pass(self.fgain, self.rf_sample_rate, 8e3, 4e3, window.WIN_HAMMING, 6.76))
        self.low_pass_filter_2.set_taps(firdes.low_pass(self.fgain, self.rf_sample_rate, 8e3, 4e3, window.WIN_HAMMING, 6.76))
        self.low_pass_filter_3.set_taps(firdes.low_pass(self.fgain, self.rf_sample_rate, 8e3, 4e3, window.WIN_HAMMING, 6.76))
        self.low_pass_filter_4.set_taps(firdes.low_pass(self.fgain, self.rf_sample_rate, 8e3, 4e3, window.WIN_HAMMING, 6.76))
        self.low_pass_filter_5.set_taps(firdes.low_pass(self.fgain, self.rf_sample_rate, 8e3, 4e3, window.WIN_HAMMING, 6.76))
        self.low_pass_filter_5_0.set_taps(firdes.low_pass(self.fgain, self.rf_sample_rate, 8e3, 4e3, window.WIN_HAMMING, 6.76))
        self.low_pass_filter_5_1.set_taps(firdes.low_pass(self.fgain, self.rf_sample_rate, 8e3, 4e3, window.WIN_HAMMING, 6.76))
        self.low_pass_filter_5_1_0.set_taps(firdes.low_pass(self.fgain, self.rf_sample_rate, 8e3, 4e3, window.WIN_HAMMING, 6.76))
        self.low_pass_filter_5_1_0_0.set_taps(firdes.low_pass(self.fgain, self.rf_sample_rate, 8e3, 4e3, window.WIN_HAMMING, 6.76))
        self.low_pass_filter_5_1_0_1.set_taps(firdes.low_pass(self.fgain, self.rf_sample_rate, 8e3, 4e3, window.WIN_HAMMING, 6.76))
        self.low_pass_filter_5_1_0_1_0.set_taps(firdes.low_pass(self.fgain, self.rf_sample_rate, 8e3, 4e3, window.WIN_HAMMING, 6.76))
        self.low_pass_filter_5_1_0_1_1.set_taps(firdes.low_pass(self.fgain, self.rf_sample_rate, 8e3, 4e3, window.WIN_HAMMING, 6.76))
        self.low_pass_filter_5_1_0_2.set_taps(firdes.low_pass(self.fgain, self.rf_sample_rate, 8e3, 4e3, window.WIN_HAMMING, 6.76))

    def get_af_sample_rate(self):
        return self.af_sample_rate

    def set_af_sample_rate(self, af_sample_rate):
        self.af_sample_rate = af_sample_rate
        self.set_fir_interp((int)(self.rf_sample_rate/self.af_sample_rate))

    def get_start_rf(self):
        return self.start_rf

    def set_start_rf(self, start_rf):
        self.start_rf = start_rf
        self.analog_sig_source_x_0.set_frequency(self.start_rf+1)
        self.analog_sig_source_x_1.set_frequency(self.start_rf+90e3)
        self.analog_sig_source_x_2.set_frequency(self.start_rf+(2*90e3))
        self.analog_sig_source_x_3.set_frequency(self.start_rf+(3*90e3))
        self.analog_sig_source_x_4.set_frequency(self.start_rf+(4*90e3))
        self.analog_sig_source_x_5.set_frequency(self.start_rf+(5*90e3))
        self.analog_sig_source_x_5_0.set_frequency(self.start_rf+(6*90e3))
        self.analog_sig_source_x_5_1.set_frequency(self.start_rf+(7*90e3))
        self.analog_sig_source_x_5_1_0.set_frequency(self.start_rf+(8*90e3))
        self.analog_sig_source_x_5_1_0_0.set_frequency(self.start_rf+(10*90e3)+(1*45e3))
        self.analog_sig_source_x_5_1_0_1.set_frequency(self.start_rf+(10*90e3)+(2*45e3))
        self.analog_sig_source_x_5_1_0_1_0.set_frequency(self.start_rf+(9*90e3))
        self.analog_sig_source_x_5_1_0_1_1.set_frequency(self.start_rf+(10*90e3)+(3*45e3))
        self.analog_sig_source_x_5_1_0_2.set_frequency(self.start_rf+(10*90e3))

    def get_fir_interp(self):
        return self.fir_interp

    def set_fir_interp(self, fir_interp):
        self.fir_interp = fir_interp

    def get_fgain(self):
        return self.fgain

    def set_fgain(self, fgain):
        self.fgain = fgain
        self.low_pass_filter_0.set_taps(firdes.low_pass(self.fgain, self.rf_sample_rate, 8e3, 4e3, window.WIN_HAMMING, 6.76))
        self.low_pass_filter_1.set_taps(firdes.low_pass(self.fgain, self.rf_sample_rate, 8e3, 4e3, window.WIN_HAMMING, 6.76))
        self.low_pass_filter_2.set_taps(firdes.low_pass(self.fgain, self.rf_sample_rate, 8e3, 4e3, window.WIN_HAMMING, 6.76))
        self.low_pass_filter_3.set_taps(firdes.low_pass(self.fgain, self.rf_sample_rate, 8e3, 4e3, window.WIN_HAMMING, 6.76))
        self.low_pass_filter_4.set_taps(firdes.low_pass(self.fgain, self.rf_sample_rate, 8e3, 4e3, window.WIN_HAMMING, 6.76))
        self.low_pass_filter_5.set_taps(firdes.low_pass(self.fgain, self.rf_sample_rate, 8e3, 4e3, window.WIN_HAMMING, 6.76))
        self.low_pass_filter_5_0.set_taps(firdes.low_pass(self.fgain, self.rf_sample_rate, 8e3, 4e3, window.WIN_HAMMING, 6.76))
        self.low_pass_filter_5_1.set_taps(firdes.low_pass(self.fgain, self.rf_sample_rate, 8e3, 4e3, window.WIN_HAMMING, 6.76))
        self.low_pass_filter_5_1_0.set_taps(firdes.low_pass(self.fgain, self.rf_sample_rate, 8e3, 4e3, window.WIN_HAMMING, 6.76))
        self.low_pass_filter_5_1_0_0.set_taps(firdes.low_pass(self.fgain, self.rf_sample_rate, 8e3, 4e3, window.WIN_HAMMING, 6.76))
        self.low_pass_filter_5_1_0_1.set_taps(firdes.low_pass(self.fgain, self.rf_sample_rate, 8e3, 4e3, window.WIN_HAMMING, 6.76))
        self.low_pass_filter_5_1_0_1_0.set_taps(firdes.low_pass(self.fgain, self.rf_sample_rate, 8e3, 4e3, window.WIN_HAMMING, 6.76))
        self.low_pass_filter_5_1_0_1_1.set_taps(firdes.low_pass(self.fgain, self.rf_sample_rate, 8e3, 4e3, window.WIN_HAMMING, 6.76))
        self.low_pass_filter_5_1_0_2.set_taps(firdes.low_pass(self.fgain, self.rf_sample_rate, 8e3, 4e3, window.WIN_HAMMING, 6.76))




def main(top_block_cls=am_xmit_multi_carrier_fl2k, options=None):
    tb = top_block_cls()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        sys.exit(0)

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    tb.start()

    try:
        input('Press Enter to quit: ')
    except EOFError:
        pass
    tb.stop()
    tb.wait()


if __name__ == '__main__':
    main()
