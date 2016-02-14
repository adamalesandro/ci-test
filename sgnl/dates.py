from datetime import date, timedelta


def prev_weekday(source_date=None):
    if source_date is None:
        source_date = date.today()

    _offsets = (3, 1, 1, 1, 1, 1, 2)

    return source_date - timedelta(days=_offsets[source_date.weekday()])


def to_mmddyy(d):
    return d.strftime("%m%d%y")