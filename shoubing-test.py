import pygame

pygame.init()


# 这是一个简单的类，用于把文字显示到屏幕上。
# 它与joysticks无关，只是为了输出一些信息。
class TextPrint:
    def __init__(self):
        self.reset()
        self.font = pygame.font.Font(None, 25)

    def tprint(self, screen, text):
        text_bitmap = self.font.render(text, True, (0, 0, 0))
        screen.blit(text_bitmap, (self.x, self.y))
        self.y += self.line_height

    def reset(self):
        self.x = 10
        self.y = 10
        self.line_height = 15

    def indent(self):
        self.x += 10

    def unindent(self):
        self.x -= 10


def main():
    # 设置窗口尺寸，并设置标题
    screen = pygame.display.set_mode((500, 700))
    pygame.display.set_caption("Joystick example")

    # 用于控制屏幕的刷新速度
    clock = pygame.time.Clock()

    # 准备打印
    text_print = TextPrint()

    # 这个字典可以保持原样，
    # 因为pygame将为程序开始时连接的每个操纵杆生成一个
    # pygame.JOYDEVICEADDED事件。
    joysticks = {}

    done = False
    while not done:
        # 处理事件
        # 可能的游戏手柄事件：JOYAXISMOTION, JOYBALLMOTION, JOYBUTTONDOWN,
        # JOYBUTTONUP, JOYHATMOTION, JOYDEVICEADDED, JOYDEVICEREMOVED
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True  # 退出循环

            if event.type == pygame.JOYBUTTONDOWN:
                print("Joystick button pressed.")
                if event.button == 0:
                    joystick = joysticks[event.instance_id]
                    if joystick.rumble(0, 0.7, 500):
                        print(f"Rumble effect played on joystick {event.instance_id}")

            if event.type == pygame.JOYBUTTONUP:
                print("Joystick button released.")

            # 处理游戏手柄的热插拔
            if event.type == pygame.JOYDEVICEADDED:
                # 该事件将在程序启动每个操纵杆时生成，无需手动创建即可填充列表。
                joy = pygame.joystick.Joystick(event.device_index)
                joysticks[joy.get_instance_id()] = joy
                print(f"Joystick {joy.get_instance_id()} connencted")

            if event.type == pygame.JOYDEVICEREMOVED:
                del joysticks[event.instance_id]
                print(f"Joystick {event.instance_id} disconnected")

        # 清除屏幕为白色
        screen.fill((255, 255, 255))
        text_print.reset()

        # 获取游戏手柄的数量
        joystick_count = pygame.joystick.get_count()

        text_print.tprint(screen, f"Number of joysticks: {joystick_count}")
        text_print.indent()

        # 遍历所有的游戏手柄
        for joystick in joysticks.values():
            jid = joystick.get_instance_id()

            text_print.tprint(screen, f"Joystick {jid}")
            text_print.indent()

            # 从操作系统中获取控制器/操纵杆的名称
            name = joystick.get_name()
            text_print.tprint(screen, f"Joystick name: {name}")

            guid = joystick.get_guid()
            text_print.tprint(screen, f"GUID: {guid}")

            power_level = joystick.get_power_level()
            text_print.tprint(screen, f"Joystick's power level: {power_level}")

            # 通常轴是成对运行的，一个是上/下，另一个是左/右。触发器算作轴。
            axes = joystick.get_numaxes()
            text_print.tprint(screen, f"Number of axes: {axes}")
            text_print.indent()

            for i in range(axes):
                axis = joystick.get_axis(i)
                text_print.tprint(screen, f"Axis {i} value: {axis:>6.3f}")
            text_print.unindent()

            buttons = joystick.get_numbuttons()
            text_print.tprint(screen, f"Number of buttons: {buttons}")
            text_print.indent()

            for i in range(buttons):
                button = joystick.get_button(i)
                text_print.tprint(screen, f"Button {i:>2} value: {button}")
            text_print.unindent()

            hats = joystick.get_numhats()
            text_print.tprint(screen, f"Number of hats: {hats}")
            text_print.indent()

            # 帽子的位置。方向要么全有要么全无，而不是像get_axis()那样的浮点数。
            # Position是一个由int值(x, y)组成的元组。
            for i in range(hats):
                hat = joystick.get_hat(i)
                text_print.tprint(screen, f"Hat {i} value: {str(hat)}")
            text_print.unindent()

            text_print.unindent()

        # 刷新屏幕
        pygame.display.flip()

        # 控制30帧每秒
        clock.tick(30)


if __name__ == "__main__":
    main()
    pygame.quit()