uint8_t calc_checksum(uint8_t *array, uint8_t len)
{
        uint32_t checksum = 0;
            checksum = array[0];
                for (int i = 1; i < len; i++)
                        {
                                    checksum += array[i];
                                        }
                    return (uint8_t)checksum % 256;
}
