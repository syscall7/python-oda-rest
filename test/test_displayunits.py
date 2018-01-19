from oda_rest.api import DisplayUnit
from test.test_case import MkdirTestCase

class TestDisplayUnits(MkdirTestCase):

    def test_displayunits(self):
        expected = (
            DisplayUnit(section_name='.text', vma=4200752, rawBytes='31ed', instStr='xor    ebp,ebp', branch='', branch_label='', opcode='xor', operands='ebp,ebp', stringRef=None, branchRef={'vma': 4200752}, targetRef=None, crossRef=[], isBranch=False, isFunction=True, labelName='abc', isCode=True),
            DisplayUnit(section_name='.text', vma=4200754, rawBytes='4989d1', instStr='mov    r9,rdx', branch='', branch_label='', opcode='mov', operands='r9,rdx', stringRef=None, branchRef=None, targetRef=None, crossRef=[], isBranch=False, isFunction=False, labelName='abc', isCode=True),
            DisplayUnit(section_name='.text', vma=4200757, rawBytes='5e', instStr='pop    rsi', branch='', branch_label='', opcode='pop', operands='rsi', stringRef=None, branchRef=None, targetRef=None, crossRef=[], isBranch=False, isFunction=False, labelName='abc', isCode=True),
            DisplayUnit(section_name='.text', vma=4200758, rawBytes='4889e2', instStr='mov    rdx,rsp', branch='', branch_label='', opcode='mov', operands='rdx,rsp', stringRef=None, branchRef=None, targetRef=None, crossRef=[], isBranch=False, isFunction=False, labelName='abc', isCode=True),
            DisplayUnit(section_name='.text', vma=4200761, rawBytes='4883e4f0', instStr='and    rsp,0xfffffffffffffff0', branch='', branch_label='', opcode='and', operands='rsp,0xfffffffffffffff0', stringRef=None, branchRef=None, targetRef=None, crossRef=[], isBranch=False, isFunction=False, labelName='abc', isCode=True),
            DisplayUnit(section_name='.text', vma=4200765, rawBytes='50', instStr='push   rax', branch='', branch_label='', opcode='push', operands='rax', stringRef=None, branchRef=None, targetRef=None, crossRef=[], isBranch=False, isFunction=False, labelName='abc', isCode=True),
            DisplayUnit(section_name='.text', vma=4200766, rawBytes='54', instStr='push   rsp', branch='', branch_label='', opcode='push', operands='rsp', stringRef=None, branchRef=None, targetRef=None, crossRef=[], isBranch=False, isFunction=False, labelName='abc', isCode=True),
            DisplayUnit(section_name='.text', vma=4200767, rawBytes='49c7c010c64000', instStr='mov    r8,0x40c610', branch='', branch_label='', opcode='mov', operands='r8,0x40c610', stringRef=None, branchRef=None, targetRef=None, crossRef=[], isBranch=False, isFunction=False, labelName='abc', isCode=True),
            DisplayUnit(section_name='.text', vma=4200774, rawBytes='48c7c180c54000', instStr='mov    rcx,0x40c580', branch='', branch_label='', opcode='mov', operands='rcx,0x40c580', stringRef=None, branchRef=None, targetRef=None, crossRef=[], isBranch=False, isFunction=False, labelName='abc', isCode=True),
            DisplayUnit(section_name='.text', vma=4200781, rawBytes='48c7c7a41d4000', instStr='mov    rdi,0x401da4', branch='', branch_label='', opcode='mov', operands='rdi,0x401da4', stringRef=None, branchRef=None, targetRef=None, crossRef=[], isBranch=False, isFunction=False, labelName='abc', isCode=True),
            DisplayUnit(section_name='.text', vma=4200788, rawBytes='e867fdffff', instStr='call   ', branch='', branch_label='', opcode='call', operands='0x004016c0', stringRef=None, branchRef=None, targetRef={'vma': 4200128}, crossRef=[], isBranch=False, isFunction=False, labelName='abc', isCode=True),
            DisplayUnit(section_name='.text', vma=4200793, rawBytes='f4', instStr='hlt    ', branch='', branch_label='', opcode='hlt', operands=' ', stringRef=None, branchRef=None, targetRef=None, crossRef=[], isBranch=False, isFunction=False, labelName='abc', isCode=True),
            DisplayUnit(section_name='.text', vma=4200794, rawBytes='90', instStr='nop', branch='', branch_label='', opcode='', operands='', stringRef=None, branchRef=None, targetRef=None, crossRef=[], isBranch=False, isFunction=False, labelName='abc', isCode=True),
            DisplayUnit(section_name='.text', vma=4200795, rawBytes='90', instStr='nop', branch='', branch_label='', opcode='', operands='', stringRef=None, branchRef=None, targetRef=None, crossRef=[], isBranch=False, isFunction=False, labelName='abc', isCode=True),
        )

        actual = self.project.DisplayUnits(0x401930, 100)

        for e, a in zip(expected, actual):
            self.assertEqual(e, a)
