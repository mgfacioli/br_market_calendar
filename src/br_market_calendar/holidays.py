#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = """\n""".join(['Marcelo G Facioli (mgfacioli@yahoo.com.br)'])
__version__ = "4.0.0"

##############################################################################
# 
import pandas as pd
import datetime

from typing_extensions import Self


##############################################################################
# module class

class BrHolidays(object):
    def __init__(self) -> None:
        self._url: str = 'http://www.anbima.com.br/feriados/arqs/feriados_nacionais.xls'
        self._holidays = pd.read_excel(self._url, parse_dates = True)
        self._holidays.dropna(inplace = True)
        self._holidays['Data'] = pd.to_datetime(self._holidays['Data'], dayfirst=True)
        self._holidays.set_index('Data', inplace = True)
        
    
    def get_holidays(self, begin_year: str = None, end_year: str = None) -> Self:
        if (begin_year is not None) and (end_year is None):
            self._period = self._holidays.loc[f'{begin_year}']
        elif (begin_year is not None) and (end_year is not None):
            self._period = self._holidays.loc[f'{begin_year}':f'{end_year}']
        else:
            self._period = self._holidays
            
        return self._period
        
    def get_holidays_by_weekday(self, weekday_list: list) ->   Self:
        return self._period[self._period['Dia da Semana'].isin(weekday_list)]