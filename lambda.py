anonymous_filter1 = lambda x: len(list(filter(lambda n: n == 'я' or n == 'Я', x))) >= 23

anonymous_filter = lambda x: x.lower().count('я') >= 23


print(anonymous_filter('zzzdddяяяяяdf zzzяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяя'))
