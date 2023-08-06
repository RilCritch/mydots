return {
  {
    "windwp/nvim-autopairs",
    event = "InsertEnter",
    -- opts = {}, -- this is equalent to setup({}) function
    config = function()
      require("nvim-autopairs").setup({})

      -- setting up rules
      local Rule = require("nvim-autopairs.rule")
      local npairs = require("nvim-autopairs")

      npairs.add_rule(Rule("`", "`", "-markdown"))
    end,
  },
}
