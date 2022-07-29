
def all_cycle(from_a_entry, from_b_entry, from_c_entry, from_d_entry, to_a_entry, to_b_entry, to_c_entry, to_d_entry,
              from_cvv_entry, to_cvv_entry, from_month_entry, from_year_entry, to_month_entry, to_year_entry,
              from_owner_entry, to_owner_entry):
    while True:
        number(from_a_entry, from_b_entry, from_c_entry, from_d_entry)
        number(to_a_entry, to_b_entry, to_c_entry, to_d_entry)
        cvv(from_cvv_entry)
        cvv(to_cvv_entry)
        date(from_month_entry, from_year_entry)
        date(to_month_entry, to_year_entry)
        owner(from_owner_entry)
        owner(to_owner_entry)


def number(a_entry, b_entry, c_entry, d_entry):
    if not a_entry.get().isdigit() or len(a_entry.get()) > 4:
        a_entry.delete(len(a_entry.get()) - 1)
    if not b_entry.get().isdigit() or len(b_entry.get()) > 4:
        b_entry.delete(len(b_entry.get()) - 1)
    if not c_entry.get().isdigit() or len(c_entry.get()) > 4:
        c_entry.delete(len(c_entry.get()) - 1)
    if not d_entry.get().isdigit() or len(d_entry.get()) > 4:
        d_entry.delete(len(d_entry.get()) - 1)


def cvv(cvv_entry):
    if not cvv_entry.get().isdigit() or len(cvv_entry.get()) > 3:
        cvv_entry.delete(len(cvv_entry.get()) - 1)


def date(month_entry, year_entry):
    if month_entry.get() not in ('', '0', '1', '01', '02', '03', '04', '05', '06', '07', '07', '08', '09', '10', '11',
                                 '12'):
        month_entry.delete(len(month_entry.get()) - 1)
    if not year_entry.get().isdigit() or len(year_entry.get()) > 2:
        year_entry.delete(len(year_entry.get()) - 1)


def owner(owner_entry):
    if len(owner_entry.get()) > 15:
        owner_entry.delete(len(owner_entry.get()) - 1)
