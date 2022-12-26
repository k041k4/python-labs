# Dictionary
empty_dict = {}
book1 = {'title': 'python intro', 'release': '2018'}
book2 = dict(title= 'python professional', release= '2020')
book3 = dict([['title','python ultra'], ['release', '2022']])
comments = dict([['comment','nic moc']])

print(book1, book2, book3)
print(book1['release'], book1.get('release'))
print(book1.keys(),book1.values())
print('ALL KEYS',list(book1.keys()),'\nALL VALUES',list(book1.values()))
print(comments)

#add/update item
book1.update(comments)
print(book1.keys(),book1.values())
#delete item
del book1['comment']
print(book1.keys(),book1.values())

#empty dictionary
empty_dict = comments
print(empty_dict)
empty_dict.clear()
print(empty_dict)
print(comments)
comments = dict([['comment','nic moc']])

#test value in dictionary
if 'release' in book3:
    print('TEST:', book3)

#copy to make dict muttable
books = book1.copy()
books.update(comments)
print('BOOKS:', books)
book1['title'] = 'eeeee'
books['comment'] =  'excellent'
print('BOOK1:', book1) # prove that book1.title is changed  but book1.comment is not added
print('BOOKS:', books) # prove that books.comment is changed but books.title is not
print('COMMENTS:', comments) # prove that comments is not changed (muted)
books.pop('comment')
print('BOOKS:', books) # prove that books.comment is removed
print('COMMENTS:', comments) # prove that comments is not changed (muted)

print('\n')
#for iterations
for book_attribute, book_value in books.items():
    print('ATTRIBUTE:',book_attribute, 'VALUE:', book_value)

print('DIFFERENCE:', set(books).difference(set(books)))
