import sys
with open('c:\\Users\\HP-LAPTOP\\Desktop\\menu\\index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

start_index = -1
end_index = -1

for i, line in enumerate(lines):
    if '<h2 data-protected="true">ENTRADAS</h2>' in line:
        start_index = i + 2
    if '<!-- FONDOS HEADER -->' in line:
        end_index = i

if start_index != -1 and end_index != -1:
    new_content = [
        '                    <div class="items-group">\n',
        '                        <!-- 1 -->\n',
        '                        <div class="menu-item">\n',
        '                            <div class="number-badge" data-protected="true">1</div>\n',
        '                            <div class="item-content">\n',
        '                                <div class="item-top">\n',
        '                                    <span class="item-title" data-protected="true">Tequeños rellenos a la norteña (4pz)\n',
        '                                        <span class="allergen-red">(1.7.3)</span></span>\n',
        '                                    <span class="price-tag editable">€10</span>\n',
        '                                </div>\n',
        '                                <div class="item-desc" data-protected="true">Descripción del plato pendiente de actualización...</div>\n',
        '                            </div>\n',
        '                        </div>\n',
        '                        <!-- 2 -->\n',
        '                        <div class="menu-item">\n',
        '                            <div class="number-badge" data-protected="true">2</div>\n',
        '                            <div class="item-content">\n',
        '                                <div class="item-top">\n',
        '                                    <span class="item-title" data-protected="true">Boliyucas con salsa de avocado\n',
        '                                        <span class="allergen-red">(1.7.3)</span></span>\n',
        '                                    <span class="price-tag editable">€10</span>\n',
        '                                </div>\n',
        '                                <div class="item-desc" data-protected="true">Descripción del plato pendiente de actualización...</div>\n',
        '                            </div>\n',
        '                        </div>\n',
        '                        <!-- 3 -->\n',
        '                        <div class="menu-item">\n',
        '                            <div class="number-badge" data-protected="true">3</div>\n',
        '                            <div class="item-content">\n',
        '                                <div class="item-top">\n',
        '                                    <span class="item-title" data-protected="true">Causa limeña\n',
        '                                        <span class="allergen-red">(4.8.14)</span></span>\n',
        '                                    <span class="price-tag editable">€12</span>\n',
        '                                </div>\n',
        '                                <div class="item-desc" data-protected="true">Descripción del plato pendiente de actualización...</div>\n',
        '                            </div>\n',
        '                        </div>\n',
        '                        <!-- 4 -->\n',
        '                        <div class="menu-item">\n',
        '                            <div class="number-badge" data-protected="true">4</div>\n',
        '                            <div class="item-content">\n',
        '                                <div class="item-top">\n',
        '                                    <span class="item-title" data-protected="true">Causa tres regiones\n',
        '                                        <span class="allergen-red">(2.3.10.14)</span></span>\n',
        '                                    <span class="price-tag editable">€15</span>\n',
        '                                </div>\n',
        '                                <div class="item-desc" data-protected="true">degustazione di patate peruviane ripiene di pesce, polipo e pollo</div>\n',
        '                            </div>\n',
        '                        </div>\n',
        '                        <!-- 5 -->\n',
        '                        <div class="menu-item">\n',
        '                            <div class="number-badge" data-protected="true">5</div>\n',
        '                            <div class="item-content">\n',
        '                                <div class="item-top">\n',
        '                                    <span class="item-title" data-protected="true">Papa rellena acompañado con salsa di rocoto (non picante)\n',
        '                                        <span class="allergen-red">(1.7.3)</span></span>\n',
        '                                    <span class="price-tag editable">€12</span>\n',
        '                                </div>\n',
        '                                <div class="item-desc" data-protected="true">patata ripiena con carne di manzo accompagnata da salsa di rocoto</div>\n',
        '                            </div>\n',
        '                        </div>\n',
        '                        <!-- 6 -->\n',
        '                        <div class="menu-item">\n',
        '                            <div class="number-badge" data-protected="true">6</div>\n',
        '                            <div class="item-content">\n',
        '                                <div class="item-top">\n',
        '                                    <span class="item-title" data-protected="true">Anticuchos a la griglia\n',
        '                                        <span class="allergen-red">(4.12)</span></span>\n',
        '                                    <span class="price-tag editable">€12</span>\n',
        '                                </div>\n',
        '                                <div class="item-desc" data-protected="true">cuori di manzo alla griglia con spezie peruviane, mais e patate con salsa di peperoncino rosso (rocoto)</div>\n',
        '                            </div>\n',
        '                        </div>\n',
        '                    </div>\n',
        '                </div>\n',
        '\n',
        '                <!-- COLUMN 2 -->\n',
        '                <div class="menu-column col-2">\n',
        '\n'
    ]
    final_lines = lines[:start_index] + new_content + lines[end_index:]
    with open('c:\\Users\\HP-LAPTOP\\Desktop\\menu\\index.html', 'w', encoding='utf-8') as f:
        f.writelines(final_lines)
    print(f'SUCCESS: Replaced lines from {start_index} to {end_index}')
else:
    print(f'FAILED TO FIND INDICES: start={start_index}, end={end_index}')
