#!/usr/bin/env lua


local colors = {
  black        = '#0c0e0f',
  white        = '#edeff0',
  red          = '#e89982',
  green        = '#78b892',
  blue         = '#6791c9',
  yellow       = '#ecd28b',
  gray         = '#505253',
  darkgray     = '#343637',
  lightgray    = '#7d7f80',
  inactivegray = '#141617',
}
return {
  normal = {
    a = {bg = colors.lightgray, fg = colors.black, gui = 'bold'},
    b = {bg = colors.darkgray, fg = colors.lightgray},
    c = {bg = colors.inactivegray, fg = colors.lightgray}
  },
  insert = {
    a = {bg = colors.blue, fg = colors.black, gui = 'bold'},
    b = {bg = colors.darkgray, fg = colors.lightgray},
    c = {bg = colors.inactivegray, fg = colors.gray}
  },
  visual = {
    a = {bg = colors.green, fg = colors.black, gui = 'bold'},
    b = {bg = colors.darkgray, fg = colors.lightgray},
    c = {bg = colors.inactivegray, fg = colors.gray}
  },
  replace = {
    a = {bg = colors.red, fg = colors.black, gui = 'bold'},
    b = {bg = colors.darkgray, fg = colors.lightgray},
    c = {bg = colors.inactivegray, fg = colors.gray}
  },
  command = {
    a = {bg = colors.yellow, fg = colors.black, gui = 'bold'},
    b = {bg = colors.darkgray, fg = colors.lightgray},
    c = {bg = colors.inactivegray, fg = colors.darkgray}
  },
  inactive = {
    a = {bg = colors.darkgray, fg = colors.black, gui = 'bold'},
    b = {bg = colors.darkgray, fg = colors.lightgray},
    c = {bg = colors.darkgray, fg = colors.gray}
  }
}
