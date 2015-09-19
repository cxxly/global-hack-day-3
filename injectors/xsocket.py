# vim: set fileencoding=utf-8
# Pavel Odvody <podvody@redhat.com>
#
# HICA - Host integrated container applications
#
# MIT License (C) 2015

from base.hica_base import *

class XSocketInjector(HicaInjector):
  def get_config_key(self):
    return "io.hica.xsocket_passthrough"

  def get_injected_args(self):
    return (("--xsocket-path", HicaValueType.PATH, "/tmp/.X11-unix"), 
        ("--x-display-num", HicaValueType.STRING, ":0"))

def register(context):
  context['xsocket'] = XSocketInjector()
