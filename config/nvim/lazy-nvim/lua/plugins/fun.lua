return {
  { -- screensaver
    "tamton-aquib/zone.nvim",
    config = function()
      require("zone").setup({
        style = "treadmill",
        after = 600, -- Idle timeout
        exclude_filetypes = { "TelescopePrompt", "NvimTree", "neo-tree", "dashboard", "lazy" },
        -- More options to come later

        treadmill = {
          direction = "left",
          headache = false,
          tick_time = 30, -- Lower, the faster * doesn't seem to do shit
          -- Opts for Treadmill style
        },
        epilepsy = {
          stage = "aura", -- "aura" or "ictal"
          tick_time = 100,
        },
        dvd = {
          -- text = {"line1", "line2", "line3", "etc"}
          tick_time = 100,
          -- Opts for Dvd style
        },
      })
    end,
  },

  -- { -- needs a newer version of neovim unfortunately
  --   "lewis6991/satellite.nvim",
  --   config = function()
  --     require("satellite").setup()
  --   end,
  -- },

  -- {
  --   "gorbit99/codewindow.nvim",
  --   config = function()
  --     local codewindow = require("codewindow")
  --     codewindow.setup()
  --     codewindow.apply_default_keybinds()
  --   end,
  -- },
}
