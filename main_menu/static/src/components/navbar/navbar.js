/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { NavBar } from "@web/webclient/navbar/navbar";

patch(NavBar.prototype, "main_menu/static/src/components/navbar/navbar.js", {
    setup() {
        this._super();
        const root = this.menuService.getMenuAsTree("root").childrenTree;
        this.menuApp = root.find(app => app.xmlid === "main_menu.main_menu_root");
    },
    onClickMenu() {
        this.onNavBarDropdownItemSelection(this.menuApp);
    },
});
