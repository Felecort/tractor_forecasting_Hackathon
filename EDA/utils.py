import re
import numpy as np


def fill_space_with_nans(df):
    """ Inplace """
    regex_pat = re.compile(r' *-', flags=re.IGNORECASE)
    df.replace(to_replace=regex_pat, value=np.nan, regex=True, inplace=True)


def remove_null_ros(df, additional_col="target"):   
    """ Not inplace """ 
    
    date = df["Дата и время"]
    target = df[additional_col]

    df.drop("Дата и время", axis=1, inplace=True)
    df.drop(additional_col, axis=1, inplace=True)
    
    idx = df.index[df.isnull().all(1) == 0]
    
    df["Дата и время"] = date
    df[additional_col] = target
    
    return df.iloc[idx]


cols_to_remove = ['Нагрузка на двигатель, %',
    'iButton2',
    'Крутящий момент (spn513), Нм',
    'Положение рейки ТНВД (spn51), %',
    'Расход топлива (spn183), л/ч',
    'ДВС. Температура наддувочного воздуха, °С',
    'Давление наддувочного воздуха двигателя (spn106), кПа',
    'Текущая передача (spn523)',
    'Температура масла гидравлики (spn5536), С',
    'Педаль слива (spn598)',
    "Темп.масла двиг.,°С",
    "Значение счетчика моточасов, час:мин",
    "КПП. Температура масла",
    "Уровень топлива % (spn96)",
    "Холодный старт (spn3871)",
    "Вода в топливе (spn3864)",
    "Необходимость сервисного обслуживания (spn3866)",
    "Разрешение запуска двигателя (spn3861)",
    "Термостарт (spn3862)",
    "Неисправность тормозной системы (spn3863)",
    "Аварийное давление масла КПП (spn3857)",
    'Сост.пед.сцепл.', 'Нейтраль КПП (spn3843)',
    'Стояночный тормоз (spn3842)',
    'Аварийная температура охлаждающей жидкости (spn3841)',
    'Засоренность воздушного фильтра (spn3840)',
    'Засоренность фильтра КПП (spn3847)',
    'Аварийное давление масла ДВС (spn3846)',
    'Засоренность фильтра ДВС (spn3845)',
    'Засоренность фильтра рулевого управления (spn3844)',
    'Засоренность фильтра навесного оборудования (spn3851)',
    'Недопустимый уровень масла в гидробаке (spn3850)',
    'Аварийная температура масла в гидросистеме (spn3849)',
    'Аварийное давление в I контуре тормозной системы (spn3848)',
    'Аварийное давление в II контуре тормозной системы (spn3855)',
    'Зарядка АКБ (spn3854)', 'Отопитель (spn3853)',
    'Выход блока управления двигателем (spn3852)',
    'Включение тормозков (spn3859)', 'Засоренность фильтра слива (spn3858)',
    'Аварийная температура масла ДВС(spn3856)',
    'Низкий уровень ОЖ (spn3860)',
    'Аварийная температура масла ГТР (spn3867)',
    'Подогрев топливного фильтра (spn3865)',
]

numeric_cols = ['Полож.пед.акселер.,%', 'Давл.масла двиг.,кПа', 'Обор.двиг.,об/мин',
       'КПП. Давление масла в системе смазки', 'Скорость',
       'ДВС. Давление смазки', 'ДВС. Температура охлаждающей жидкости',
       'Давление в пневмостистеме (spn46), кПа', 'Электросистема. Напряжение',
       'ДВС. Частота вращения коленчатого вала']

brake_int_cols = ["Полож.пед.акселер.,%", "Обор.двиг.,об/мин"]
