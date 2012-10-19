# -*- coding: utf-8 -*-
import os
import pprint
PP = pprint.PrettyPrinter(indent=4)
import sure

(4).should.be.equal(2 + 2)
(7.5).should.eql(3.5 + 4)
(2).should.equal(8 / 4)

(3).shouldnt.be.equal(5)


{'a': 'collection'}.should.equal({'a': 'collection'}) 

{'foo': 'bar'}.should.equal({'foo': 'bar'})
{'foo': 'bar'}.should.eql({'foo': 'bar'})
{'foo': 'bar'}.must.be.equal({'foo': 'bar'})


"A string".lower().should.equal("a string")

[].should.be.empty;
{}.should.be.empty;
set().should.be.empty;
"".should.be.empty;
().should.be.empty
range(0).should.be.empty;

[1, 2, 3].shouldnt.be.empty;
"Lincoln de Sousa".shouldnt.be.empty;
"Lincoln de Sousa".should_not.be.empty;


(1).should.be.within(0, 2)
(5).should.be.within(10)

(1).shouldnt.be.within(5, 6)

"g".should.be.within("gabriel")
'name'.should.be.within({'name': 'Gabriel'})
'Lincoln'.should.be.within(['Lincoln', 'Gabriel'])

'Bug'.shouldnt.be.within(['Sure 1.0'])
'Bug'.should_not.be.within(['Sure 1.0'])

value = None
value.should.be.none
None.should.be.none

"".should_not.be.none
(not None).should_not.be.none

from sure import this

True.should.be.ok
'truthy string'.should.be.ok
{'truthy': 'dictionary'}.should.be.ok

False.shouldnt.be.ok
''.should_not.be.ok
{}.shouldnot.be.ok



class Basket(object):
    fruits = ["apple", "banana"]
basket1 = Basket()
basket1.should.have.property("fruits")

basket2 = Basket()
basket2.should.have.property("fruits").being.equal(["apple", "banana"])
basket2.should.have.property("fruits").with_value.equal(["apple", "banana"])
basket2.should.have.property("fruits").with_value.being.equal(["apple", "banana"])


basket3 = dict(fruits=["apple", "banana"])
basket3.should.have.key("fruits")

person = dict(name=None)

person.should.have.key("name").being.none
person.should.have.key("name").being.equal(None)


[3, 4].should.have.length_of(2)
"Python".should.have.length_of(6)
{'john': 'person'}.should_not.have.length_of(2)


(5).should.be.greater_than(4)
(5).should_not.be.greater_than(10)
(1).should.be.lower_than(2)
(1).should_not.be.lower_than(0)


range.when.called_with(10, step="20").should.throw(TypeError, "range() takes no keyword arguments")
range.when.called_with("chuck norris").should.throw("range() integer end argument expected, got str.")
range.when.called_with("chuck norris").should.throw(TypeError)
range.when.called_with(10).should_not.throw(TypeError)


range.when.called_with(2).should.return_value([0, 1])

value = range(2)
value.should.equal([0, 1])

{}.should.be.a('dict')
(5).should.be.an('int')

range(10).should.be.a('collections.Iterable')

u"".should.be.an(unicode)
[].should.be.a(list)


(10).should.be.below(11)
(10).should.be.above(9)
(10).should_not.be.above(11)
(10).should_not.be.below(9)


from sure import it, this, those, these, expect

(10).should.be.equal(5 + 5)
this(10).should.be.equal(5 + 5)
it(10).should.be.equal(5 + 5)
these(10).should.be.equal(5 + 5)
those(10).should.be.equal(5 + 5)


assert (10).should.be.equal(5 + 5)
assert this(10).should.be.equal(5 + 5)
assert it(10).should.be.equal(5 + 5)
assert these(10).should.be.equal(5 + 5)
assert those(10).should.be.equal(5 + 5)

expect(10).to.be.equal(5 + 5)
expect(10).to.not_be.equal(8)


range.should.be.callable
(lambda: None).should.be.callable;
(123).should_not.be.callable


"Name".lower().should.equal('name')
assert "Name".lower().should.equal('name')
assert this("Name".lower()).should.equal('name')
this("Name".lower()).should.equal('name')

(2 + 2).should.be.equal(4)
(2 + 2).must.be.equal(4)
(2 + 2).does.equals(4)
(2 + 2).do.equals(4)

# import expect gerekiyor
(2).should_not.be.equal(3)
(2).shouldnt.be.equal(3)
(2).doesnt.equals(3)
(2).does_not.equals(3)
(2).doesnot.equals(3)
(2).dont.equal(3)
(2).do_not.equal(3)

expect(3).to.not_be.equal(1)


{"foo": 1}.must.with_value.being.equal({"foo": 1})
{"foo": 1}.does.have.key("foo").being.with_value.equal(1)

(2).should.equal(2)
(2).should.equals(2)
(2).should.eql(2)

(not None).should.be.ok
(not None).should.be.truthy
(not None).should.be.true

False.should.be.falsy
False.should.be.false
False.should_not.be.true
False.should_not.be.ok
None.should_not.be.true
None.should_not.be.ok






# PP.pprint([
#     (k, os.environ[k])
#     for k in sorted(os.environ.iterkeys())
#     ]
# )

# 