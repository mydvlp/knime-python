/*
 * ------------------------------------------------------------------------
 *
 *  Copyright by KNIME GmbH, Konstanz, Germany
 *  Website: http://www.knime.com; Email: contact@knime.com
 *
 *  This program is free software; you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License, Version 3, as
 *  published by the Free Software Foundation.
 *
 *  This program is distributed in the hope that it will be useful, but
 *  WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with this program; if not, see <http://www.gnu.org/licenses>.
 *
 *  Additional permission under GNU GPL version 3 section 7:
 *
 *  KNIME interoperates with ECLIPSE solely via ECLIPSE's plug-in APIs.
 *  Hence, KNIME and ECLIPSE are both independent programs and are not
 *  derived from each other. Should, however, the interpretation of the
 *  GNU GPL Version 3 ("License") under any applicable laws result in
 *  KNIME and ECLIPSE being a combined program, KNIME GMBH herewith grants
 *  you the additional permission to use and propagate KNIME together with
 *  ECLIPSE with only the license terms in place for ECLIPSE applying to
 *  ECLIPSE and the GNU GPL Version 3 applying for KNIME, provided the
 *  license terms of ECLIPSE themselves allow for the respective use and
 *  propagation of ECLIPSE together with KNIME.
 *
 *  Additional permission relating to nodes for KNIME that extend the Node
 *  Extension (and in particular that are based on subclasses of NodeModel,
 *  NodeDialog, and NodeView) and that only interoperate with KNIME through
 *  standard APIs ("Nodes"):
 *  Nodes are deemed to be separate and independent programs and to not be
 *  covered works.  Notwithstanding anything to the contrary in the
 *  License, the License does not apply to Nodes, you are not required to
 *  license Nodes under the License, and you are granted a license to
 *  prepare and propagate Nodes, in each case even if such Nodes are
 *  propagated with or for interoperation with KNIME.  The owner of a Node
 *  may freely choose the license terms applicable to such Node, including
 *  when such Node is propagated with or for interoperation with KNIME.
 * ---------------------------------------------------------------------
 *
 * History
 *   Aug 2, 2017 (clemens): created
 */
package org.knime.python2.serde.arrow.extractors;

import org.apache.arrow.vector.NullableIntVector;
import org.knime.python2.extensions.serializationlibrary.SerializationOptions;
import org.knime.python2.extensions.serializationlibrary.interfaces.Cell;
import org.knime.python2.extensions.serializationlibrary.interfaces.Type;
import org.knime.python2.extensions.serializationlibrary.interfaces.VectorExtractor;
import org.knime.python2.extensions.serializationlibrary.interfaces.impl.CellImpl;

/**
 * Manages the data transfer between the arrow table format and the python table format. Works on Integer vectors.
 *
 * @author Clemens von Schwerin, KNIME GmbH, Konstanz, Germany
 */
public class IntegerExtractor implements VectorExtractor {

    private final NullableIntVector.Accessor m_accessor;

    private final SerializationOptions m_serializationOptions;

    private int m_ctr;

    /**
     * Constructor.
     *
     * @param vector the vector to extract from
     * @param opts additional serialization options
     */
    public IntegerExtractor(final NullableIntVector vector, final SerializationOptions opts) {
        m_accessor = vector.getAccessor();
        m_serializationOptions = opts;
    }

    /**
     * {@inheritDoc}
     */
    @Override
    public Cell extract() {
        Cell c;
        if (m_accessor.isNull(m_ctr)) {
            c = new CellImpl();
        } else {
            int val = m_accessor.get(m_ctr);
            if (m_serializationOptions.getConvertMissingFromPython()
                && m_serializationOptions.isSentinel(Type.INTEGER, val)) {
                c = new CellImpl();
            } else {
                c = new CellImpl(val);
            }
        }
        m_ctr++;
        return c;
    }

}