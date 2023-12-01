return {
  -- disable lua_ls (no FreeBSD support)
  {
    "neovim/nvim-lspconfig",
    ---@class PluginLspOpts
    opts = {
      ---@type lspconfig.options
      servers = {
        lua_ls = { enabled = false, mason = false },
      },
    },
  },
}
