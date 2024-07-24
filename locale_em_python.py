import calendar
import locale

# muda a 'localização' do meu código para o padrão do sistema operacional
locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')
print(locale.getlocale())  # vê os locais configurados no sistema operacional
print(calendar.calendar(2024))
