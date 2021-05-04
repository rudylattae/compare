from compare3 import expect, UnmetExpectation, expect_call
import logging
from logging import Logger
logging.basicConfig(level=logging.NOTSET)
logging.root.setLevel(logging.NOTSET)



if __name__ == '__main__':

    expect.comparison_log_level=10
    expect.logger=Logger("expressions")
    expect.logger.setLevel(logging.NOTSET)

    # simple equals and contains
    expect("new value").equal_to("new value").and_.contains("val")
    # same thing but with not on first
    expect("new value").is_not_.equal_to("new value 1").and_.contains("val")
    try:
        expect(20).equal_to("apples")
    except UnmetExpectation as ue:
        expect(str(ue)).equal_to("'20' is not equal to 'apples'")

    try:
        expect(20).equal_to("apples")
    except AssertionError as ue:
        expect(str(ue)).equal_to("'20' is not equal to 'apples'")

    expect(20).is_.numeric().and_.equal_to_as_integer('20').and_.equal_to_as_integer(20).equal_to_as_strings(20)
    expect(20.01).is_.numeric().and_.equal_to_as_floating_point(20.01).and_.equal_to_as_floating_point('20.01').and_\
        .equal_to_as_strings(20.01)
    try:
        expect(20).is_not_.numeric()
    except UnmetExpectation as ue:
        expect(str(ue)).equal_to("20 seems numeric")
    expect(0).falsy()
    expect(1).truthy()
    expect(-1).truthy()

    def summer(*args):
        return sum([int(i) for i in args])

    expect_call(summer,12,50,45).returns(107)
    expect_call(summer,"25","apples","75").raises(ValueError, "invalid literal for .* 'apples'")
