#!/usr/bin/env lua

-- local variables - from luasnip docs
local ls = require("luasnip")
local s = ls.snippet
local sn = ls.snippet_node
local isn = ls.indent_snippet_node
local t = ls.text_node
local i = ls.insert_node
local f = ls.function_node
local c = ls.choice_node
local d = ls.dynamic_node
local r = ls.restore_node
local events = require("luasnip.util.events")
local ai = require("luasnip.nodes.absolute_indexer")
local extras = require("luasnip.extras")
local l = extras.lambda
local rep = extras.rep
local p = extras.partial
local m = extras.match
local n = extras.nonempty
local dl = extras.dynamic_lambda
local fmt = require("luasnip.extras.fmt").fmt
local fmta = require("luasnip.extras.fmt").fmta
local conds = require("luasnip.extras.expand_conditions")
local postfix = require("luasnip.extras.postfix").postfix
local types = require("luasnip.util.types")
local parse = require("luasnip.util.parser").parse_snippet
local ms = ls.multi_snippet
local k = require("luasnip.nodes.key_indexer").new_key
local add = ls.add_snippets

----------------------------------------------------------- help {{{
--[[ multiline text 
	-- use a list
	-- each element in the list is a new line
    -- to add different nodes other nodes and still get new lines
    --  use a blank string at begginning of next text node to specify new line
--]]
--- }}}

----------------------------------------------------------- global snippets {{{
add("all", {
	s("bang", {
		t({ "#!/usr/bin/env " }),
		i(0),
	}),
})
-- }}}

add("lua", {
	s("header", {
		t({ "-- Description: " }),
		i(1),
		t({ "", "--", "--" }),
		t({ "", "-- Author: RilCritch" }),
		t({ "", "--", "--" }),
		t({ "", "-- Date Created: " }),
		i(0), -- figure out good way to do manually
	}),
})
