# instant-decodable
# Instantaneous decodability check
Prefix codes are also known as prefix-free codes, prefix condition codes and instantaneous codes.A prefix code is a uniquely decodable code: a receiver can identify each word without requiring a special marker between words. However, there are uniquely decodable codes that are not prefix codes; for instance, the reverse of a prefix code is still uniquely decodable (it is a suffix code), but it is not necessarily a prefix code.

This program checks if a code satisfies the prefix condition and tells us if it's instantaneously decodable.

## Usage
Execute the program by typing in the following command. Where [code](code) is the name of the file containing the code.
```
python prefix.py code
```
