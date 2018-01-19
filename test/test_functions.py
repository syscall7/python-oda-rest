from test.test_case import MkdirTestCase
from oda_rest.api import Function

class TestFunctions(MkdirTestCase):

    def test_functions(self):

        expected = (
            Function(name='.init', vma=4199632, args='unknown', retval='unknown'),
            Function(name='_init', vma=4199632, args='unknown', retval='unknown'),
            Function(name='_init', vma=4199632, args='unknown', retval='unknown'),
            Function(name='.plt', vma=4199664, args='unknown', retval='unknown'),
            Function(name='func_00401500', vma=4199680, args='unknown', retval='unknown'),
            Function(name='func_00401510', vma=4199696, args='unknown', retval='unknown'),
            Function(name='func_00401520', vma=4199712, args='unknown', retval='unknown'),
            Function(name='func_00401530', vma=4199728, args='unknown', retval='unknown'),
            Function(name='func_00401540', vma=4199744, args='unknown', retval='unknown'),
            Function(name='func_00401550', vma=4199760, args='unknown', retval='unknown'),
            Function(name='func_00401560', vma=4199776, args='unknown', retval='unknown'),
            Function(name='func_00401570', vma=4199792, args='unknown', retval='unknown'),
            Function(name='func_00401580', vma=4199808, args='unknown', retval='unknown'),
            Function(name='func_00401590', vma=4199824, args='unknown', retval='unknown'),
            Function(name='func_004015a0', vma=4199840, args='unknown', retval='unknown'),
            Function(name='func_004015b0', vma=4199856, args='unknown', retval='unknown'),
            Function(name='func_004015c0', vma=4199872, args='unknown', retval='unknown'),
            Function(name='func_004015d0', vma=4199888, args='unknown', retval='unknown'),
            Function(name='func_004015e0', vma=4199904, args='unknown', retval='unknown'),
            Function(name='func_004015f0', vma=4199920, args='unknown', retval='unknown'),
            Function(name='func_00401600', vma=4199936, args='unknown', retval='unknown'),
            Function(name='func_00401610', vma=4199952, args='unknown', retval='unknown'),
            Function(name='func_00401620', vma=4199968, args='unknown', retval='unknown'),
            Function(name='func_00401630', vma=4199984, args='unknown', retval='unknown'),
            Function(name='func_00401640', vma=4200000, args='unknown', retval='unknown'),
            Function(name='func_00401650', vma=4200016, args='unknown', retval='unknown'),
            Function(name='func_00401660', vma=4200032, args='unknown', retval='unknown'),
            Function(name='func_00401670', vma=4200048, args='unknown', retval='unknown'),
            Function(name='func_00401680', vma=4200064, args='unknown', retval='unknown'),
            Function(name='func_00401690', vma=4200080, args='unknown', retval='unknown'),
            Function(name='func_004016a0', vma=4200096, args='unknown', retval='unknown'),
            Function(name='func_004016b0', vma=4200112, args='unknown', retval='unknown'),
            Function(name='func_004016c0', vma=4200128, args='unknown', retval='unknown'),
            Function(name='func_004016d0', vma=4200144, args='unknown', retval='unknown'),
            Function(name='func_004016e0', vma=4200160, args='unknown', retval='unknown'),
            Function(name='func_004016f0', vma=4200176, args='unknown', retval='unknown'),
            Function(name='func_00401700', vma=4200192, args='unknown', retval='unknown'),
            Function(name='func_00401710', vma=4200208, args='unknown', retval='unknown'),
            Function(name='func_00401720', vma=4200224, args='unknown', retval='unknown'),
            Function(name='func_00401730', vma=4200240, args='unknown', retval='unknown'),
            Function(name='func_00401740', vma=4200256, args='unknown', retval='unknown'),
            Function(name='func_00401750', vma=4200272, args='unknown', retval='unknown'),
            Function(name='func_00401760', vma=4200288, args='unknown', retval='unknown'),
            Function(name='func_00401780', vma=4200320, args='unknown', retval='unknown'),
            Function(name='func_00401790', vma=4200336, args='unknown', retval='unknown'),
            Function(name='func_004017a0', vma=4200352, args='unknown', retval='unknown'),
            Function(name='func_004017b0', vma=4200368, args='unknown', retval='unknown'),
            Function(name='func_004017d0', vma=4200400, args='unknown', retval='unknown'),
            Function(name='func_004017e0', vma=4200416, args='unknown', retval='unknown'),
            Function(name='func_004017f0', vma=4200432, args='unknown', retval='unknown'),
            Function(name='func_00401800', vma=4200448, args='unknown', retval='unknown'),
            Function(name='func_00401810', vma=4200464, args='unknown', retval='unknown'),
            Function(name='func_00401820', vma=4200480, args='unknown', retval='unknown'),
            Function(name='func_00401830', vma=4200496, args='unknown', retval='unknown'),
            Function(name='func_00401840', vma=4200512, args='unknown', retval='unknown'),
            Function(name='func_00401850', vma=4200528, args='unknown', retval='unknown'),
            Function(name='func_00401860', vma=4200544, args='unknown', retval='unknown'),
            Function(name='func_00401870', vma=4200560, args='unknown', retval='unknown'),
            Function(name='func_00401880', vma=4200576, args='unknown', retval='unknown'),
            Function(name='func_00401890', vma=4200592, args='unknown', retval='unknown'),
            Function(name='func_004018a0', vma=4200608, args='unknown', retval='unknown'),
            Function(name='func_004018b0', vma=4200624, args='unknown', retval='unknown'),
            Function(name='func_004018d0', vma=4200656, args='unknown', retval='unknown'),
            Function(name='func_004018e0', vma=4200672, args='unknown', retval='unknown'),
            Function(name='func_004018f0', vma=4200688, args='unknown', retval='unknown'),
            Function(name='func_00401900', vma=4200704, args='unknown', retval='unknown'),
            Function(name='func_00401910', vma=4200720, args='unknown', retval='unknown'),
            Function(name='func_00401920', vma=4200736, args='unknown', retval='unknown'),
            Function(name='.text', vma=4200752, args='unknown', retval='unknown'),
            Function(name='_start', vma=4200752, args='unknown', retval='unknown'),
            Function(name='call_gmon_start', vma=4200796, args='unknown', retval='unknown'),
            Function(name='call_gmon_start', vma=4200796, args='unknown', retval='unknown'),
            Function(name='__do_global_dtors_aux', vma=4200832, args='unknown', retval='unknown'),
            Function(name='__do_global_dtors_aux', vma=4200832, args='unknown', retval='unknown'),
            Function(name='frame_dummy', vma=4200944, args='unknown', retval='unknown'),
            Function(name='frame_dummy', vma=4200944, args='unknown', retval='unknown'),
            Function(name='emit_mandatory_arg_note', vma=4200980, args='unknown', retval='unknown'),
            Function(name='emit_mandatory_arg_note', vma=4200980, args='unknown', retval='unknown'),
            Function(name='emit_ancillary_info', vma=4201027, args='unknown', retval='unknown'),
            Function(name='emit_ancillary_info', vma=4201027, args='unknown', retval='unknown'),
            Function(name='emit_try_help', vma=4201314, args='unknown', retval='unknown'),
            Function(name='emit_try_help', vma=4201314, args='unknown', retval='unknown'),
            Function(name='usage', vma=4201376, args='unknown', retval='unknown'),
            Function(name='usage', vma=4201376, args='unknown', retval='unknown'),
            Function(name='announce_mkdir', vma=4201581, args='unknown', retval='unknown'),
            Function(name='announce_mkdir', vma=4201581, args='unknown', retval='unknown'),
            Function(name='make_ancestor', vma=4201666, args='unknown', retval='unknown'),
            Function(name='process_dir', vma=4201771, args='unknown', retval='unknown'),
            Function(name='main', vma=4201892, args='unknown', retval='unknown'),
            Function(name='prog_fprintf', vma=4202644, args='unknown', retval='unknown'),
            Function(name='prog_fprintf', vma=4202644, args='unknown', retval='unknown'),
            Function(name='close_stdout_set_file_name', vma=4202892, args='unknown', retval='unknown'),
            Function(name='close_stdout_set_ignore_EPIPE', vma=4202913, args='unknown', retval='unknown'),
            Function(name='close_stdout', vma=4202934, args='unknown', retval='unknown'),
            Function(name='last_component', vma=4203172, args='unknown', retval='unknown'),
            Function(name='last_component', vma=4203172, args='unknown', retval='unknown'),
            Function(name='base_len', vma=4203277, args='unknown', retval='unknown'),
            Function(name='make_dir_parents', vma=4203376, args='unknown', retval='unknown'),
            Function(name='make_dir_parents', vma=4203376, args='unknown', retval='unknown'),
            Function(name='octal_to_mode', vma=4204436, args='unknown', retval='unknown'),
            Function(name='octal_to_mode', vma=4204436, args='unknown', retval='unknown'),
            Function(name='make_node_op_equals', vma=4204448, args='unknown', retval='unknown'),
            Function(name='make_node_op_equals', vma=4204448, args='unknown', retval='unknown'),
            Function(name='mode_compile', vma=4204540, args='unknown', retval='unknown'),
            Function(name='mode_compile', vma=4204540, args='unknown', retval='unknown'),
            Function(name='mode_create_from_ref', vma=4205604, args='unknown', retval='unknown'),
            Function(name='mode_adjust', vma=4205675, args='unknown', retval='unknown'),
            Function(name='mode_adjust', vma=4205675, args='unknown', retval='unknown'),
            Function(name='set_program_name', vma=4206084, args='unknown', retval='unknown'),
            Function(name='set_program_name', vma=4206084, args='unknown', retval='unknown'),
            Function(name='clone_quoting_options', vma=4206360, args='unknown', retval='unknown'),
            Function(name='get_quoting_style', vma=4206433, args='unknown', retval='unknown'),
            Function(name='set_quoting_style', vma=4206463, args='unknown', retval='unknown'),
            Function(name='set_char_quoting', vma=4206499, args='unknown', retval='unknown'),
            Function(name='set_char_quoting', vma=4206499, args='unknown', retval='unknown'),
            Function(name='set_quoting_flags', vma=4206641, args='unknown', retval='unknown'),
            Function(name='set_custom_quoting', vma=4206692, args='unknown', retval='unknown'),
            Function(name='set_custom_quoting', vma=4206692, args='unknown', retval='unknown'),
            Function(name='quoting_options_from_style', vma=4206782, args='unknown', retval='unknown'),
            Function(name='quoting_options_from_style', vma=4206782, args='unknown', retval='unknown'),
            Function(name='gettext_quote', vma=4206902, args='unknown', retval='unknown'),
            Function(name='gettext_quote', vma=4206902, args='unknown', retval='unknown'),
            Function(name='quotearg_buffer_restyled', vma=4207070, args='unknown', retval='unknown'),
            Function(name='quotearg_buffer_restyled', vma=4207070, args='unknown', retval='unknown'),
            Function(name='quotearg_buffer', vma=4209937, args='unknown', retval='unknown'),
            Function(name='quotearg_alloc', vma=4210097, args='unknown', retval='unknown'),
            Function(name='quotearg_alloc_mem', vma=4210147, args='unknown', retval='unknown'),
            Function(name='quotearg_alloc_mem', vma=4210147, args='unknown', retval='unknown'),
            Function(name='quotearg_free', vma=4210447, args='unknown', retval='unknown'),
            Function(name='quotearg_n_options', vma=4210612, args='unknown', retval='unknown'),
            Function(name='quotearg_n_options', vma=4210612, args='unknown', retval='unknown'),
            Function(name='quotearg_n', vma=4211233, args='unknown', retval='unknown'),
            Function(name='quotearg_n', vma=4211233, args='unknown', retval='unknown'),
            Function(name='quotearg_n_mem', vma=4211276, args='unknown', retval='unknown'),
            Function(name='quotearg_n_mem', vma=4211276, args='unknown', retval='unknown'),
            Function(name='quotearg', vma=4211320, args='unknown', retval='unknown'),
            Function(name='quotearg_mem', vma=4211351, args='unknown', retval='unknown'),
            Function(name='quotearg_n_style', vma=4211390, args='unknown', retval='unknown'),
            Function(name='quotearg_n_style', vma=4211390, args='unknown', retval='unknown'),
            Function(name='quotearg_n_style_mem', vma=4211455, args='unknown', retval='unknown'),
            Function(name='quotearg_n_style_mem', vma=4211455, args='unknown', retval='unknown'),
            Function(name='quotearg_style', vma=4211518, args='unknown', retval='unknown'),
            Function(name='quotearg_style_mem', vma=4211554, args='unknown', retval='unknown'),
            Function(name='quotearg_char_mem', vma=4211598, args='unknown', retval='unknown'),
            Function(name='quotearg_char_mem', vma=4211598, args='unknown', retval='unknown'),
            Function(name='quotearg_char', vma=4211746, args='unknown', retval='unknown'),
            Function(name='quotearg_char', vma=4211746, args='unknown', retval='unknown'),
            Function(name='quotearg_colon', vma=4211788, args='unknown', retval='unknown'),
            Function(name='quotearg_colon', vma=4211788, args='unknown', retval='unknown'),
            Function(name='quotearg_colon_mem', vma=4211819, args='unknown', retval='unknown'),
            Function(name='quotearg_n_custom', vma=4211861, args='unknown', retval='unknown'),
            Function(name='quotearg_n_custom', vma=4211861, args='unknown', retval='unknown'),
            Function(name='quotearg_n_custom_mem', vma=4211915, args='unknown', retval='unknown'),
            Function(name='quotearg_n_custom_mem', vma=4211915, args='unknown', retval='unknown'),
            Function(name='quotearg_custom', vma=4212066, args='unknown', retval='unknown'),
            Function(name='quotearg_custom_mem', vma=4212113, args='unknown', retval='unknown'),
            Function(name='quote_n_mem', vma=4212171, args='unknown', retval='unknown'),
            Function(name='quote_n_mem', vma=4212171, args='unknown', retval='unknown'),
            Function(name='quote_mem', vma=4212215, args='unknown', retval='unknown'),
            Function(name='quote_n', vma=4212254, args='unknown', retval='unknown'),
            Function(name='quote_n', vma=4212254, args='unknown', retval='unknown'),
            Function(name='quote', vma=4212295, args='unknown', retval='unknown'),
            Function(name='quote', vma=4212295, args='unknown', retval='unknown'),
            Function(name='savewd_init', vma=4212328, args='unknown', retval='unknown'),
            Function(name='savewd_init', vma=4212328, args='unknown', retval='unknown'),
            Function(name='savewd_errno', vma=4212348, args='unknown', retval='unknown'),
            Function(name='savewd_errno', vma=4212348, args='unknown', retval='unknown'),
            Function(name='savewd_save', vma=4212383, args='unknown', retval='unknown'),
            Function(name='savewd_save', vma=4212383, args='unknown', retval='unknown'),
            Function(name='savewd_chdir', vma=4212720, args='unknown', retval='unknown'),
            Function(name='savewd_chdir', vma=4212720, args='unknown', retval='unknown'),
            Function(name='savewd_restore', vma=4213145, args='unknown', retval='unknown'),
            Function(name='savewd_restore', vma=4213145, args='unknown', retval='unknown'),
            Function(name='savewd_finish', vma=4213490, args='unknown', retval='unknown'),
            Function(name='savewd_finish', vma=4213490, args='unknown', retval='unknown'),
            Function(name='savewd_delegating', vma=4213618, args='unknown', retval='unknown'),
            Function(name='savewd_delegating', vma=4213618, args='unknown', retval='unknown'),
            Function(name='savewd_process_files', vma=4213662, args='unknown', retval='unknown'),
            Function(name='savewd_process_files', vma=4213662, args='unknown', retval='unknown'),
            Function(name='getcon', vma=4214004, args='unknown', retval='unknown'),
            Function(name='freecon', vma=4214034, args='unknown', retval='unknown'),
            Function(name='getfscreatecon', vma=4214044, args='unknown', retval='unknown'),
            Function(name='setfscreatecon', vma=4214074, args='unknown', retval='unknown'),
            Function(name='setfscreatecon', vma=4214074, args='unknown', retval='unknown'),
            Function(name='matchpathcon', vma=4214104, args='unknown', retval='unknown'),
            Function(name='getfilecon', vma=4214141, args='unknown', retval='unknown'),
            Function(name='lgetfilecon', vma=4214175, args='unknown', retval='unknown'),
            Function(name='fgetfilecon', vma=4214209, args='unknown', retval='unknown'),
            Function(name='setfilecon', vma=4214242, args='unknown', retval='unknown'),
            Function(name='lsetfilecon', vma=4214276, args='unknown', retval='unknown'),
            Function(name='fsetfilecon', vma=4214310, args='unknown', retval='unknown'),
            Function(name='security_check_context', vma=4214343, args='unknown', retval='unknown'),
            Function(name='security_check_context_raw', vma=4214373, args='unknown', retval='unknown'),
            Function(name='setexeccon', vma=4214403, args='unknown', retval='unknown'),
            Function(name='security_compute_create', vma=4214433, args='unknown', retval='unknown'),
            Function(name='matchpathcon_init_prefix', vma=4214477, args='unknown', retval='unknown'),
            Function(name='version_etc_arn', vma=4214512, args='unknown', retval='unknown'),
            Function(name='version_etc_arn', vma=4214512, args='unknown', retval='unknown'),
            Function(name='version_etc_ar', vma=4215994, args='unknown', retval='unknown'),
            Function(name='version_etc_va', vma=4216097, args='unknown', retval='unknown'),
            Function(name='version_etc_va', vma=4216097, args='unknown', retval='unknown'),
            Function(name='version_etc', vma=4216314, args='unknown', retval='unknown'),
            Function(name='version_etc', vma=4216314, args='unknown', retval='unknown'),
            Function(name='emit_bug_reporting_address', vma=4216496, args='unknown', retval='unknown'),
            Function(name='xnmalloc', vma=4216604, args='unknown', retval='unknown'),
            Function(name='xnmalloc', vma=4216604, args='unknown', retval='unknown'),
            Function(name='xnrealloc', vma=4216666, args='unknown', retval='unknown'),
            Function(name='x2nrealloc', vma=4216742, args='unknown', retval='unknown'),
            Function(name='x2nrealloc', vma=4216742, args='unknown', retval='unknown'),
            Function(name='xcharalloc', vma=4216907, args='unknown', retval='unknown'),
            Function(name='xcharalloc', vma=4216907, args='unknown', retval='unknown'),
            Function(name='xmalloc', vma=4216933, args='unknown', retval='unknown'),
            Function(name='xmalloc', vma=4216933, args='unknown', retval='unknown'),
            Function(name='xrealloc', vma=4216986, args='unknown', retval='unknown'),
            Function(name='xrealloc', vma=4216986, args='unknown', retval='unknown'),
            Function(name='x2realloc', vma=4217083, args='unknown', retval='unknown'),
            Function(name='xzalloc', vma=4217125, args='unknown', retval='unknown'),
            Function(name='xcalloc', vma=4217168, args='unknown', retval='unknown'),
            Function(name='xmemdup', vma=4217225, args='unknown', retval='unknown'),
            Function(name='xmemdup', vma=4217225, args='unknown', retval='unknown'),
            Function(name='xstrdup', vma=4217277, args='unknown', retval='unknown'),
            Function(name='xalloc_die', vma=4217352, args='unknown', retval='unknown'),
            Function(name='xalloc_die', vma=4217352, args='unknown', retval='unknown'),
            Function(name='rpl_vfprintf', vma=4217408, args='unknown', retval='unknown'),
            Function(name='rpl_vfprintf', vma=4217408, args='unknown', retval='unknown'),
            Function(name='c_strcasecmp', vma=4217772, args='unknown', retval='unknown'),
            Function(name='c_strcasecmp', vma=4217772, args='unknown', retval='unknown'),
            Function(name='close_stream', vma=4217896, args='unknown', retval='unknown'),
            Function(name='close_stream', vma=4217896, args='unknown', retval='unknown'),
            Function(name='open_safer', vma=4218036, args='unknown', retval='unknown'),
            Function(name='open_safer', vma=4218036, args='unknown', retval='unknown'),
            Function(name='get_charset_aliases', vma=4218312, args='unknown', retval='unknown'),
            Function(name='get_charset_aliases', vma=4218312, args='unknown', retval='unknown'),
            Function(name='locale_charset', vma=4219700, args='unknown', retval='unknown'),
            Function(name='locale_charset', vma=4219700, args='unknown', retval='unknown'),
            Function(name='mkancesdirs', vma=4219988, args='unknown', retval='unknown'),
            Function(name='mkancesdirs', vma=4219988, args='unknown', retval='unknown'),
            Function(name='dirchownmod', vma=4220440, args='unknown', retval='unknown'),
            Function(name='dirchownmod', vma=4220440, args='unknown', retval='unknown'),
            Function(name='fd_safer', vma=4221012, args='unknown', retval='unknown'),
            Function(name='fd_safer', vma=4221012, args='unknown', retval='unknown'),
            Function(name='rpl_fclose', vma=4221092, args='unknown', retval='unknown'),
            Function(name='rpl_fclose', vma=4221092, args='unknown', retval='unknown'),
            Function(name='clear_ungetc_buffer_preserving_position', vma=4221276, args='unknown', retval='unknown'),
            Function(name='clear_ungetc_buffer_preserving_position', vma=4221276, args='unknown', retval='unknown'),
            Function(name='rpl_fflush', vma=4221327, args='unknown', retval='unknown'),
            Function(name='rpl_fflush', vma=4221327, args='unknown', retval='unknown'),
            Function(name='rpl_fseeko', vma=4221404, args='unknown', retval='unknown'),
            Function(name='rpl_fseeko', vma=4221404, args='unknown', retval='unknown'),
            Function(name='fseterr', vma=4221588, args='unknown', retval='unknown'),
            Function(name='fseterr', vma=4221588, args='unknown', retval='unknown'),
            Function(name='decimal_point_char', vma=4221616, args='unknown', retval='unknown'),
            Function(name='decimal_point_char', vma=4221616, args='unknown', retval='unknown'),
            Function(name='is_infinite_or_zerol', vma=4221665, args='unknown', retval='unknown'),
            Function(name='is_infinite_or_zerol', vma=4221665, args='unknown', retval='unknown'),
            Function(name='vasnprintf', vma=4221734, args='unknown', retval='unknown'),
            Function(name='vasnprintf', vma=4221734, args='unknown', retval='unknown'),
            Function(name='c_isascii', vma=4235744, args='unknown', retval='unknown'),
            Function(name='c_isalnum', vma=4235777, args='unknown', retval='unknown'),
            Function(name='c_isalpha', vma=4235832, args='unknown', retval='unknown'),
            Function(name='c_isblank', vma=4235875, args='unknown', retval='unknown'),
            Function(name='c_iscntrl', vma=4235908, args='unknown', retval='unknown'),
            Function(name='c_isdigit', vma=4235945, args='unknown', retval='unknown'),
            Function(name='c_islower', vma=4235978, args='unknown', retval='unknown'),
            Function(name='c_isgraph', vma=4236011, args='unknown', retval='unknown'),
            Function(name='c_isprint', vma=4236044, args='unknown', retval='unknown'),
            Function(name='c_ispunct', vma=4236077, args='unknown', retval='unknown'),
            Function(name='c_isspace', vma=4236144, args='unknown', retval='unknown'),
            Function(name='c_isupper', vma=4236201, args='unknown', retval='unknown'),
            Function(name='c_isxdigit', vma=4236234, args='unknown', retval='unknown'),
            Function(name='c_tolower', vma=4236289, args='unknown', retval='unknown'),
            Function(name='c_tolower', vma=4236289, args='unknown', retval='unknown'),
            Function(name='c_toupper', vma=4236321, args='unknown', retval='unknown'),
            Function(name='dup_safer', vma=4236356, args='unknown', retval='unknown'),
            Function(name='dup_safer', vma=4236356, args='unknown', retval='unknown'),
            Function(name='xsum', vma=4236396, args='unknown', retval='unknown'),
            Function(name='xsum', vma=4236396, args='unknown', retval='unknown'),
            Function(name='xsum3', vma=4236448, args='unknown', retval='unknown'),
            Function(name='xsum4', vma=4236504, args='unknown', retval='unknown'),
            Function(name='xsum4', vma=4236504, args='unknown', retval='unknown'),
            Function(name='xmax', vma=4236579, args='unknown', retval='unknown'),
            Function(name='xmax', vma=4236579, args='unknown', retval='unknown'),
            Function(name='rpl_fcntl', vma=4236608, args='unknown', retval='unknown'),
            Function(name='rpl_fcntl', vma=4236608, args='unknown', retval='unknown'),
            Function(name='rpl_isnanl', vma=4237312, args='unknown', retval='unknown'),
            Function(name='rpl_isnanl', vma=4237312, args='unknown', retval='unknown'),
            Function(name='printf_fetchargs', vma=4237404, args='unknown', retval='unknown'),
            Function(name='printf_fetchargs', vma=4237404, args='unknown', retval='unknown'),
            Function(name='printf_parse', vma=4239424, args='unknown', retval='unknown'),
            Function(name='printf_parse', vma=4239424, args='unknown', retval='unknown'),
            Function(name='__libc_csu_init', vma=4244864, args='unknown', retval='unknown'),
            Function(name='__libc_csu_fini', vma=4245008, args='unknown', retval='unknown'),
            Function(name='atexit', vma=4245024, args='unknown', retval='unknown'),
            Function(name='atexit', vma=4245024, args='unknown', retval='unknown'),
            Function(name='__stat', vma=4245056, args='unknown', retval='unknown'),
            Function(name='stat', vma=4245056, args='unknown', retval='unknown'),
            Function(name='__fstat', vma=4245072, args='unknown', retval='unknown'),
            Function(name='fstat', vma=4245072, args='unknown', retval='unknown'),
            Function(name='__do_global_ctors_aux', vma=4245088, args='unknown', retval='unknown'),
            Function(name='__do_global_ctors_aux', vma=4245088, args='unknown', retval='unknown'),
            Function(name='.fini', vma=4245144, args='unknown', retval='unknown'),
            Function(name='_fini', vma=4245144, args='unknown', retval='unknown'),
        )

        actual = self.project.Functions()

        self.assertEqual(len(expected), len(actual))
