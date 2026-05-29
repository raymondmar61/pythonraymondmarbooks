'''
Hashing is transforming any given key or a string of characters into another value. The result is normally a shorter, fixed-length value that makes it computationally easier to work with than the original key.  Hashmaps, also known as hashtables, represent one of the most common implementations of hashing. Hashmaps stores key-value pairs (e.g., employee ID and employee name) in a list that is accessible through its index. A hashmap is an indexed data structure or a data structure that leverages hashing techniques to store data in an associative fashion. They are optimized data structures that allow faster data operations, including insertion, deletion, and search.  Hashmaps distribute the entries (key/value pairs) across an array of buckets. Given a key, a hashing function will compute a distinct index that suggests where the entry can be found.

An illustration described in words.  Three keys.  The hash function matches each of the three keys with its index number and its value.  Key 1 goes to the hash function which matches with index 3 and value 4.  Key 2 goes to the hash function which matches with index 2 and value 3.  Key 3 goes to the hash function which matches with index 0 and value 1.

Hashmaps vs dictionaries. A dictionary is just Python's native implementation of hashmaps; in other words, dictionaries are hashmaps. While a hashmap is a data structure that can be created using multiple hashing techniques, a dictionary is a particular, Python-based hashmap, whose design and behavior are specified in the Python's dict class.

The dictionary implements a hash map hashmap.  The dictionary stores data in key and value pairs.  Extreme fast data retrieval typically O(1) time complexity on average.  Hashing:  Python uses a hash function to convert a unique, immutable key into an index in an underlying array.  The keys must be immutable or unchangeable.  Keys must be unique.  If two different keys produce the same hash, Python uses a strategy called open addressing to find the next available slot.  Multiple key-value pairs are stored in the same list or linked list.

The standard hash map operations uses dictionary syntax:  initialize mymap={} or mymap=dict().  Insert or update mymap["key"]="value".  Access value=mymap["key"] or mymap.get("key").  Delete del mymap["key"] or mymap.pop("key").  Check existence "key" in mymap.

The collections module offers specialized versions.  defaultdict automatically initializes a key with a default value if it doesn't exist yet.  OrderedDict specifically maintains the order in which items were inserted.  Counter is a subclass of dict designed for counting hashable objects.
'''
#Two ways to create a dictionary
createdictionary1 = {"name": "William", "age": 28, "city": "Cairo"}
print(createdictionary1) #print {'name': 'William', 'age': 28, 'city': 'Cairo'}
createdictionary2constructor = dict(name="William", age=28, city="Cairo")
print(createdictionary2constructor) #print {'name': 'William', 'age': 28, 'city': 'Cairo'}
hashmapdictionary = {}
print(hashmapdictionary) #print {}
hashmapdictionary["insertkey1"] = "insertvalue1"
hashmapdictionary["insertkey2"] = "insertvalue2"
hashmapdictionary["insertkey3"] = "insertvalue3"
print(hashmapdictionary) #print {'insertkey1': 'insertvalue1', 'insertkey2': 'insertvalue2', 'insertkey3': 'insertvalue3'}
print(hashmapdictionary["insertkey1"]) #print insertvalue1
del hashmapdictionary["insertkey2"]
print(hashmapdictionary) #print {'insertkey1': 'insertvalue1', 'insertkey3': 'insertvalue3'}
hashmapdictionary["insertkey3"] = "insertvalue3" #Attempt duplicate key-value entry.
print(hashmapdictionary) #print {'insertkey1': 'insertvalue1', 'insertkey3': 'insertvalue3'}.  No repeats.
hashmapdictionary["insertkey3"] = "insertvalue33"
print(hashmapdictionary) #print {'insertkey1': 'insertvalue1', 'insertkey3': 'insertvalue33'}.  The key exists.  The key's value is updated from insertvalue3 to insertvalue33.
getavalue = hashmapdictionary["insertkey3"]
print(getavalue) #print insertvalue33
hashmapdictionary2 = dict()
print(hashmapdictionary2) #print {}
hashmapdictionary2["insertkey1"] = "insertvalue1"
print(hashmapdictionary2.get("insertkey1")) #print insertvalue1.  The get() method returns None if the key doesn't exist.  No error message appears when retrieving a value for which the key doesn't exist.
hashmapdictionary2["insertkey2"] = "insertvalue2"
hashmapdictionary2["insertkey3"] = "insertvalue3"
print(hashmapdictionary2) #print {'insertkey1': 'insertvalue1', 'insertkey2': 'insertvalue2', 'insertkey3': 'insertvalue3'}
hashmapdictionary2["insertkey4"] = ["multiple","values","forinsertvalue4"]
print(hashmapdictionary2) #print {'insertkey1': 'insertvalue1', 'insertkey2': 'insertvalue2', 'insertkey3': 'insertvalue3', 'insertkey4': ['multiple', 'values', 'forinsertvalue4']}
hashmapdictionary2["insertkey4"].append("append another value to a key with multiple values")
print(hashmapdictionary2) #print {'insertkey1': 'insertvalue1', 'insertkey2': 'insertvalue2', 'insertkey3': 'insertvalue3', 'insertkey4': ['multiple', 'values', 'forinsertvalue4', 'append another value to a key with multiple values']}
hashmapdictionary2.pop("insertkey1")
print(hashmapdictionary2) #print {'insertkey2': 'insertvalue2', 'insertkey3': 'insertvalue3', 'insertkey4': ['multiple', 'values', 'forinsertvalue4', 'append another value to a key with multiple values']}
hashmapdictionary2["assigntruevalue"] = True
print(hashmapdictionary2) #print {'insertkey2': 'insertvalue2', 'insertkey3': 'insertvalue3', 'insertkey4': ['multiple', 'values', 'forinsertvalue4', 'append another value to a key with multiple values'], 'assigntruevalue': True}
hashmapdictionary2.clear()
print(hashmapdictionary2) #print {}
hashmapdictionary2["justcleardictionary"] = "Delete entire contents in a dictionary"
print(hashmapdictionary2) #print {'justcleardictionary': 'Delete entire contents in a dictionary'}
hashmapdictionary2["addanentry"] = "Loop a dictionary looping a dictionary"
print(hashmapdictionary2.items()) #print dict_items([('justcleardictionary', 'Delete entire contents in a dictionary'), ('addanentry', 'Loop a dictionary looping a dictionary')])
for key, value in hashmapdictionary2.items():
    print(f"key {key}, value {value}")
    '''
    key justcleardictionary, value Delete entire contents in a dictionary
    key addanentry, value Loop a dictionary looping a dictionary
    '''
print(hashmapdictionary2.keys()) #print dict_keys(['justcleardictionary', 'addanentry'])
for eachkey in hashmapdictionary2.keys():
    print(eachkey) #print justcleardictionary\n addanentry
print(hashmapdictionary2.values()) #print dict_values(['Delete entire contents in a dictionary', 'Loop a dictionary looping a dictionary'])
from collections import defaultdict
alternatehashmapimplementation = defaultdict(lambda: "Default value instead of an error is The key doesn't exist")
alternatehashmapimplementation["createdefaultdict"] = "defaultdict in collections module"
alternatehashmapimplementation["builtindictionaries"] = "defaultdict and dictionaries are almost the same"
print(alternatehashmapimplementation) #print defaultdict(<function <lambda> at 0x7ac1ed586560>, {'createdefaultdict': 'defaultdict in collections module', 'builtindictionaries': 'defaultdict and dictionaries are almost the same'})
print(alternatehashmapimplementation["createdefaultdict"]) #print defaultdict in collections module
print(alternatehashmapimplementation["keydoesntexist"]) #print Default value instead of an error is The key doesn't exist
from collections import Counter
#Counter is a dictionary where elements are stored as keys and their counts are stored as values
iterablecounter = Counter(['aaa', 'bbb', 'aaa', 'ccc', 'ccc', 'aaa'])
mapcounter = Counter({'red': 4, 'blue': 2})
keywordargumentscounter = Counter(cats=4, dogs=8)
print(iterablecounter) #print Counter({'aaa': 3, 'ccc': 2, 'bbb': 1})
print(mapcounter) #print Counter({'red': 4, 'blue': 2})
print(keywordargumentscounter) #print Counter({'dogs': 8, 'cats': 4})
print(f"Counter keys {keywordargumentscounter.keys()}") #print Counter keys dict_keys(['cats', 'dogs'])
print(f"Counter values {keywordargumentscounter.values()}") #print  ounter values dict_values([4, 8])
print(f"list all elements {list(keywordargumentscounter.elements())}") #print list all elements ['cats', 'cats', 'cats', 'cats', 'dogs', 'dogs', 'dogs', 'dogs', 'dogs', 'dogs', 'dogs', 'dogs']
print(f"count elements {iterablecounter.total()}") #print count elements 6
print(f"2 most common elements {keywordargumentscounter.most_common(2)}") #print 2 most common elements [('dogs', 8), ('cats', 4)]
