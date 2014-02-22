# -*- coding: utf-8 -*-



# Copyright 2014 Frederic Bergeron. All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without modification, are
# permitted provided that the following conditions are met:
# 
#    1. Redistributions of source code must retain the above copyright notice, this list of
#       conditions and the following disclaimer.
# 
#    2. Redistributions in binary form must reproduce the above copyright notice, this list
#       of conditions and the following disclaimer in the documentation and/or other materials
#       provided with the distribution.
# 
# THIS SOFTWARE IS PROVIDED BY Frederic Bergeron ``AS IS'' AND ANY EXPRESS OR IMPLIED
# WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
# FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL Frederic Bergeron OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
# ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
# ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# 
# The views and conclusions contained in the software and documentation are those of the
# authors and should not be interpreted as representing official policies, either expressed
# or implied, of Frederic Bergeron.


class BBcode:

    def __init__( self ):
        pass

    def surroundByCoord(self,list):
        result = []
        for line in list:
            if len(line) == 6:
                newline = '[coord]' + line[:3] + '|' + line[3:] + '[/coord]'
            else:
                newline = '[coord]' + line + '[/coord]'
            result.append(newline)
        return result

    def surroundByPlayer(self,list):
        result = []
        for line in list:
            newline = '[player]' + line + '[/player]'
            result.append(newline)
        return result

    def surroundByAlly(self,list):
        result = []
        for line in list:
            newline = '[ally]' + line + '[/ally]'
            result.append(newline)
        return result

    def surroundByReport(self,list):
        result = []
        for line in list:
            newline = '[report]' + line + '[/report]'
            result.append(newline)
        return result

    def surroundByReportDisplay(self,list):
        result = []
        for line in list:
            newline = '[report_display]' + line + '[/report_display]'
            result.append(newline)
        return result
