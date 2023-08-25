return {
  {
    "catppuccin/nvim",
    name = "catppuccin",
    priority = 1000,
    opts = {
      flavour = "mocha", -- latte, frappe, macchiato, mocha
      color_overrides = {
        mocha = {
          base = "#181825",
          mantle = "#1e1e2e",
        },
      },
      integrations = {
        aerial = true,
        markdown = true,
        nvimtree = true,
        rainbow_delimiters = true,
        bufferline = true,
      },
    },
  },

  -- Configure LazyVim to load gruvbox
  {
    "LazyVim/LazyVim",
    opts = {
      -- colorscheme = "tokyonight",
      -- colorscheme = "nordic",
      colorscheme = "catppuccin",
    },
  },
}
