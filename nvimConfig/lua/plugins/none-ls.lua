return {
    "nvimtools/none-ls.nvim",
    config = function()
        local null_ls = require("null-ls")
        null_ls.setup({
            sources = {
                null_ls.builtins.formatting.stylua, -- Lua formatter
                null_ls.builtins.completion.spell, -- Spell suggestions completions source
                -- null_ls.builtins.diagnostics.cppcheck, -- C/C++ analyzer
                null_ls.builtins.formatting.clang_format, -- C/C++/... formatter
                null_ls.builtins.formatting.black, -- Python formatter
                -- null_ls.builtins.diagnostics.vale, -- LaTeX linter
            },
        })

        vim.keymap.set("n", "<leader>gf", vim.lsp.buf.format, { desc = "Format file" })
    end,
}
